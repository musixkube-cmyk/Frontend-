import Link from "next/link";

export default function AdvertisePage() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      <div className="flex min-h-screen flex-col items-center justify-center gap-8 px-6">
        <img
          src="/musicosy-logo.png"
          alt="Musicosy"
          className="w-32 object-contain opacity-80"
        />
        <h1 className="font-display text-4xl font-bold tracking-tight">Self-Service Ad Portal</h1>
        <p className="max-w-md text-center text-muted-foreground">
          Reach the audience that fits your sound. Create campaigns, target listeners, and track results — your self-service advertising portal is coming soon.
        </p>
        <Link
          href="/signin"
          className="rounded-full bg-primary px-6 py-3 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
        >
          Get started
        </Link>
        <Link
          href="/"
          className="text-sm text-muted-foreground transition-colors hover:text-foreground"
        >
          ← Back to home
        </Link>
      </div>
    </main>
  );
}
