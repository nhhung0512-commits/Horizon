-- Grants required because tables were created via the Management API, which
-- does not apply Supabase's default-privilege GRANTs the way its own
-- migration/dashboard flow does.

grant usage on schema public to anon, authenticated, service_role;

-- papers: public read (RLS policy already restricts anon/authenticated to SELECT),
-- service_role needs full access to write from push_to_supabase.py
grant select on public.papers to anon, authenticated;
grant select, insert, update, delete on public.papers to service_role;

-- topics, notes: locked down to service_role only (no RLS policies for anon/authenticated)
grant select, insert, update, delete on public.topics to service_role;
grant select, insert, update, delete on public.notes to service_role;
