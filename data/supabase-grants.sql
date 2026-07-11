-- Grants required because tables were created via the Management API, which
-- does not apply Supabase's default-privilege GRANTs the way its own
-- migration/dashboard flow does.

grant usage on schema public to anon, authenticated, service_role;

-- papers: public read (RLS policy already restricts anon/authenticated to SELECT),
-- service_role needs full access to write from push_to_supabase.py
grant select on public.papers to anon, authenticated;
grant select, insert, update, delete on public.papers to service_role;

-- topics: public read too, needed for the dashboard's topic filter dropdown.
-- Writes remain service_role only.
grant select on public.topics to anon, authenticated;
grant select, insert, update, delete on public.topics to service_role;

-- notes: signed-in users can read/write their own rows (enforced by RLS
-- policies using auth.uid()); service_role keeps full access.
grant select, insert, update on public.notes to authenticated;
grant select, insert, update, delete on public.notes to service_role;

-- mof_data: public read (manually compiled research data), writes are
-- service_role only (imported via script, not user-editable).
grant select on public.mof_data to anon, authenticated;
grant select, insert, update, delete on public.mof_data to service_role;
