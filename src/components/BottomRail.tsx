import Link from "next/link";

const rails: {
  label: string;
  links: { label: string; to: string }[];
}[] = [
  {
    label: "Community",
    links: [
      { label: "Community hub", to: "/community" },
      { label: "Community guidelines", to: "/community/guidelines" },
      { label: "Safety & reporting", to: "/community/safety" },
      { label: "Creator support", to: "/community/support" },
    ],
  },
  {
    label: "Legal",
    links: [
      { label: "Terms of service", to: "/legal/terms" },
      { label: "Privacy policy", to: "/legal/privacy" },
      { label: "Rights & royalties", to: "/legal/rights" },
      { label: "Copyright / DMCA", to: "/legal/copyright" },
    ],
  },
  {
    label: "Advertising space",
    links: [
      { label: "For creators", to: "/advertising/creators" },
      { label: "For businesses", to: "/advertising/businesses" },
      { label: "For labels", to: "/advertising/labels" },
      { label: "Advertising overview", to: "/advertising" },
    ],
  },
  {
    label: "Get on Musicosy",
    links: [
      { label: "Start onboarding", to: "/onboarding" },
      { label: "Label or roster account", to: "/onboarding/business" },
      { label: "Sync & licensing", to: "/for/sync-agents" },
      { label: "Distribution partners", to: "/for/distributors" },
    ],
  },
];

export function BottomRail() {
  return (
    <footer className="mt-24 bg-ink text-ink-foreground">
      <div className="mx-auto w-full max-w-6xl px-6 py-14">
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
          {rails.map((rail) => (
            <nav key={rail.label} aria-label={rail.label}>
              <h3 className="text-xs font-semibold uppercase tracking-[0.18em] text-primary">
                {rail.label}
              </h3>
              <ul className="mt-4 space-y-2.5">
                {rail.links.map((link) => (
                  <li key={link.to}>
                    <Link
                      href={link.to}
                      className="text-sm text-ink-muted transition-colors hover:text-ink-foreground"
                    >
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </nav>
          ))}
        </div>

        <div className="mt-12 grid grid-cols-[minmax(0,1fr)_auto] items-center gap-4 border-t border-white/10 pt-6 sm:flex sm:justify-between">
          <div className="flex min-w-0 items-center gap-3">
            <img
              src="/musicosy-orange-logo.webp"
              alt="Musicosy"
              className="h-7 w-auto object-contain"
            />
            <p className="truncate text-xs text-ink-muted">
              Everything music. One place.
            </p>
          </div>
          <p className="text-xs text-ink-muted">&copy; {new Date().getFullYear()} Musicosy</p>
        </div>
      </div>
    </footer>
  );
}
