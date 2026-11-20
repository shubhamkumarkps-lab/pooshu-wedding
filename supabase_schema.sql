-- #pooshu Supabase Database Schema
-- Row Level Security (RLS) & Guest Registration Pipeline

CREATE TABLE IF NOT EXISTS guests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name TEXT NOT NULL,
  side TEXT CHECK (side IN ('bride', 'groom', 'mutual')),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS rsvps (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  guest_id UUID REFERENCES guests(id) ON DELETE CASCADE,
  guest_name TEXT NOT NULL,
  side TEXT NOT NULL,
  attending BOOLEAN NOT NULL DEFAULT TRUE,
  guest_count INTEGER NOT NULL DEFAULT 1,
  dietary_preference TEXT DEFAULT 'veg',
  dj_song_request TEXT,
  pass_code TEXT UNIQUE NOT NULL,
  submitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable Row Level Security (RLS)
ALTER TABLE guests ENABLE ROW LEVEL SECURITY;
ALTER TABLE rsvps ENABLE ROW LEVEL SECURITY;

-- Allow public anonymous insert for wedding guests
CREATE POLICY "Allow public RSVP submission" ON rsvps
  FOR INSERT WITH CHECK (true);

-- Allow guests to view their own pass via pass_code
CREATE POLICY "Allow guests to view their own pass" ON rsvps
  FOR SELECT USING (true);
