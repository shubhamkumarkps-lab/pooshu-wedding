import zlib, struct, math

def unfilter_scanline(filter_type, cur, prev, bpp):
    recon = bytearray(len(cur))
    for i in range(len(cur)):
        a = recon[i - bpp] if i >= bpp else 0
        b = prev[i] if prev else 0
        c = prev[i - bpp] if (prev and i >= bpp) else 0
        
        if filter_type == 0: # None
            val = cur[i]
        elif filter_type == 1: # Sub
            val = (cur[i] + a) & 0xff
        elif filter_type == 2: # Up
            val = (cur[i] + b) & 0xff
        elif filter_type == 3: # Average
            val = (cur[i] + ((a + b) // 2)) & 0xff
        elif filter_type == 4: # Paeth
            p = a + b - c
            pa = abs(p - a)
            pb = abs(p - b)
            pc = abs(p - c)
            if pa <= pb and pa <= pc:
                pr = a
            elif pb <= pc:
                pr = b
            else:
                pr = c
            val = (cur[i] + pr) & 0xff
        else:
            val = cur[i]
        recon[i] = val
    return recon

def process_seal(src_path, dst_path):
    with open(src_path, 'rb') as f:
        data = f.read()

    pos = 8
    width, height = 0, 0
    idat_data = b''
    color_type = 2
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        ctype = data[pos+4:pos+8]
        cdata = data[pos+8:pos+8+length]
        pos += 8 + length + 4
        if ctype == b'IHDR':
            width, height, bit_depth, color_type = struct.unpack('>IIBB', cdata[:10])
        elif ctype == b'IDAT':
            idat_data += cdata

    raw = zlib.decompress(idat_data)
    src_bpp = 3 if color_type == 2 else 4
    src_stride = 1 + width * src_bpp

    cx, cy = width / 2.0, height / 2.0
    radius = min(cx, cy) * 0.485 # slightly tighter to trim any edge artifacts

    out_raw = bytearray()
    prev_recon = None

    for y in range(height):
        filter_type = raw[y * src_stride]
        cur_line = raw[y * src_stride + 1 : (y + 1) * src_stride]
        recon = unfilter_scanline(filter_type, cur_line, prev_recon, src_bpp)
        prev_recon = recon

        # Build output line with filter 0 (None), RGBA
        out_raw.append(0)
        dy = y - cy
        for x in range(width):
            dx = x - cx
            dist = math.hypot(dx, dy)

            r = recon[x * src_bpp]
            g = recon[x * src_bpp + 1]
            b = recon[x * src_bpp + 2]

            # White background detection (corners)
            is_white = (r > 240 and g > 240 and b > 240)

            # Circular feathering
            if dist > radius:
                alpha = 0
            elif dist > radius - 2:
                # 2px anti-aliasing feather
                feather = (radius - dist) / 2.0
                alpha = int(255 * max(0.0, min(1.0, feather)))
                if is_white:
                    alpha = 0
            elif is_white and dist > radius * 0.90:
                alpha = 0
            else:
                alpha = 255

            out_raw.extend([r, g, b, alpha])

    # Compress new IDAT
    new_idat = zlib.compress(bytes(out_raw), 9)

    def make_chunk(ctype, cdata):
        chunk = ctype + cdata
        crc = zlib.crc32(chunk) & 0xffffffff
        return struct.pack('>I', len(cdata)) + chunk + struct.pack('>I', crc)

    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0) # 6 = RGBA

    with open(dst_path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        f.write(make_chunk(b'IHDR', ihdr_data))
        f.write(make_chunk(b'IDAT', new_idat))
        f.write(make_chunk(b'IEND', b''))

    print(f'Successfully cropped {src_path} -> {dst_path} ({width}x{height} RGBA)')

process_seal('New Assets/Wax Seal 1.png', 'public/assets/wax_seal_real.png')
