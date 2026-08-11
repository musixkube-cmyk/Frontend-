import Link from "next/link";

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      <div className="flex min-h-screen flex-col items-center justify-center gap-8 px-6">
        <img
          src="/musicosy-logo.png"
          alt="Musicosy"
          className="w-32 object-contain opacity-80"
        />
        <h1 className="font-display text-4xl font-bold tracking-tight">My Dashboard</h1>
        <p className="max-w-md text-center text-muted-foreground">
          Your dashboard is being built. Stream stats, catalog management, earnings and more — all landing here.
        </p>
        <Link
          href="/"
          className="rounded-full bg-primary px-6 py-3 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
        >
          Back to home
        </Link>
      </div>
    </main>
  );
}
