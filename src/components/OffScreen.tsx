"use client";

import Link from "next/link";
import { useState } from "react";
import { entryBySlug, entries } from "@/lib/entries";

interface OffScreenProps {
  slug: string;
}

type AuthMode = "signin" | "signup";

export function OffScreen({ slug }: OffScreenProps) {
  const entry = entryBySlug(slug);
  if (!entry) return null;

  const [mode, setMode] = useState<AuthMode>("signin");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [phone, setPhone] = useState("");
  const [showPhone, setShowPhone] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const isSignIn = mode === "signin";

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);

    // Simulate auth delay — replace with real auth later
    await new Promise((r) => setTimeout(r, 800));

    if (isSignIn) {
      if (!email.trim() || !password.trim()) {
        setError("Enter your email and password.");
        setLoading(false);
        return;
      }
    } else {
      if (!email.trim() || !password.trim() || !displayName.trim()) {
        setError("Fill in all fields to create your account.");
        setLoading(false);
        return;
      }
    }

    // Redirect to home on success
    window.location.href = "/";
  }

  function handleOAuth(provider: string) {
    // Placeholder — will wire to real OAuth
    setLoading(true);
    setTimeout(() => {
      window.location.href = "/";
    }, 600);
  }

  return (
    <main className="light min-h-screen bg-background">
      <div className="px-6 pt-8 md:px-12">
        <Link
          href="/"
          className="font-display text-xs uppercase tracking-[0.3em] text-muted-foreground transition-colors hover:text-foreground"
        >
          ← Back
        </Link>
      </div>

      <div className="mx-auto grid max-w-7xl grid-cols-1 items-center gap-16 px-6 py-14 md:px-12 lg:grid-cols-[1.15fr_0.85fr] lg:gap-24 lg:py-24">
        {/* Left: logo + messaging */}
        <div>
          <img
            src="/musicosy-logo.png"
            alt="Musicosy"
            className="w-full max-w-[420px] lg:max-w-[560px]"
          />
          <p className="mt-10 font-display text-xs uppercase tracking-[0.4em] text-muted-foreground">
            {entry.num} · {entry.label}
          </p>
          <h1 className="mt-4 font-display text-[13vw] leading-[0.88] tracking-tight text-foreground sm:text-6xl lg:text-7xl xl:text-8xl">
            {entry.headline}
          </h1>
          <p className="mt-6 max-w-md text-base text-muted-foreground">{entry.sub}</p>
        </div>

        {/* Right: auth panel */}
        <div className="w-full max-w-md justify-self-center lg:justify-self-end">
          {/* Mode toggle */}
          <div className="mb-8 flex rounded-full border border-border p-1">
            <button
              type="button"
              onClick={() => { setMode("signin"); setError(""); }}
              className={`flex-1 rounded-full py-2.5 text-sm font-medium transition-colors ${
                isSignIn
                  ? "bg-primary text-primary-foreground"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              Sign in
            </button>
            <button
              type="button"
              onClick={() => { setMode("signup"); setError(""); }}
              className={`flex-1 rounded-full py-2.5 text-sm font-medium transition-colors ${
                !isSignIn
                  ? "bg-primary text-primary-foreground"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              Create account
            </button>
          </div>

          {/* OAuth buttons */}
          <button
            type="button"
            onClick={() => setShowPhone(!showPhone)}
            className="flex h-14 w-full items-center justify-center gap-3 rounded-full bg-primary font-medium text-primary-foreground transition-opacity hover:opacity-90"
          >
            <PhoneIcon /> Continue with phone
          </button>

          {showPhone && (
            <div className="mt-3">
              <input
                type="tel"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                placeholder="+1 (555) 000-0000"
                className="h-14 w-full rounded-xl border border-border bg-background px-4 text-base text-foreground placeholder:text-muted-foreground focus:border-ring focus:outline-none"
              />
              <button
                type="button"
                onClick={() => handleOAuth("phone")}
                disabled={!phone.trim()}
                className="mt-2 h-12 w-full rounded-full bg-primary font-medium text-primary-foreground transition-opacity hover:opacity-90 disabled:bg-muted disabled:text-muted-foreground"
              >
                Send code
              </button>
            </div>
          )}

          <button
            type="button"
            onClick={() => handleOAuth("google")}
            disabled={loading}
            className="mt-3 flex h-14 w-full items-center justify-center gap-3 rounded-full border border-border bg-background font-medium text-foreground transition-colors hover:bg-secondary disabled:opacity-50"
          >
            <GoogleIcon /> Continue with Google
          </button>

          <button
            type="button"
            onClick={() => handleOAuth("apple")}
            disabled={loading}
            className="mt-3 flex h-14 w-full items-center justify-center gap-3 rounded-full border border-border bg-background font-medium text-foreground transition-colors hover:bg-secondary disabled:opacity-50"
          >
            <AppleIcon /> Continue with Apple
          </button>

          <div className="my-6 flex items-center gap-4">
            <span className="h-px flex-1 bg-border" />
            <span className="text-sm text-muted-foreground">or</span>
            <span className="h-px flex-1 bg-border" />
          </div>

          {/* Email form */}
          <form onSubmit={handleSubmit}>
            {!isSignIn && (
              <div className="mb-3">
                <label htmlFor="displayName" className="sr-only">
                  Display name
                </label>
                <input
                  id="displayName"
                  type="text"
                  value={displayName}
                  onChange={(e) => setDisplayName(e.target.value)}
                  placeholder="Display name"
                  className="h-14 w-full rounded-xl border border-border bg-background px-4 text-base text-foreground placeholder:text-muted-foreground focus:border-ring focus:outline-none"
                />
              </div>
            )}

            <label htmlFor="identifier" className="sr-only">
              Email
            </label>
            <input
              id="identifier"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Email"
              className="h-14 w-full rounded-xl border border-border bg-background px-4 text-base text-foreground placeholder:text-muted-foreground focus:border-ring focus:outline-none"
            />

            <label htmlFor="password" className="sr-only">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
              className="mt-3 h-14 w-full rounded-xl border border-border bg-background px-4 text-base text-foreground placeholder:text-muted-foreground focus:border-ring focus:outline-none"
            />

            {isSignIn && (
              <p className="mt-2 text-right">
                <button
                  type="button"
                  className="text-xs font-medium text-muted-foreground transition-colors hover:text-foreground"
                >
                  Forgot password?
                </button>
              </p>
            )}

            {error && (
              <p className="mt-3 text-center text-sm text-destructive">{error}</p>
            )}

            <button
              type="submit"
              disabled={loading}
              className="mt-4 h-14 w-full rounded-full bg-primary font-medium text-primary-foreground transition-opacity hover:opacity-90 disabled:bg-muted disabled:text-muted-foreground"
            >
              {loading ? (
                <span className="inline-flex items-center gap-2">
                  <SpinnerIcon /> {isSignIn ? "Signing in…" : "Creating account…"}
                </span>
              ) : isSignIn ? (
                "Sign in"
              ) : (
                "Create account"
              )}
            </button>
          </form>

          <p className="mt-5 text-center text-xs leading-relaxed text-muted-foreground">
            By continuing, you agree to our{" "}
            <span className="font-semibold text-foreground">Terms of Service</span>,{" "}
            <span className="font-semibold text-foreground">Privacy Policy</span> and{" "}
            <span className="font-semibold text-foreground">Cookie Use</span>.
          </p>

          <div className="mt-10 flex flex-wrap justify-center gap-x-4 gap-y-2">
            {entries
              .filter((e) => e.slug !== entry.slug)
              .map((e) => (
                <Link
                  key={e.slug}
                  href={`/${e.slug}`}
                  className="font-display text-[11px] uppercase tracking-[0.2em] text-muted-foreground transition-colors hover:text-foreground"
                >
                  {e.label}
                </Link>
              ))}
          </div>
        </div>
      </div>
    </main>
  );
}

function PhoneIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z" />
    </svg>
  );
}

function GoogleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">
      <path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.5a5.6 5.6 0 0 1-2.4 3.7v3h3.9c2.3-2.1 3.5-5.2 3.5-8.9z" />
      <path fill="#34A853" d="M12 24c3.2 0 5.9-1.1 7.9-2.9l-3.9-3c-1.1.7-2.4 1.2-4 1.2-3.1 0-5.7-2.1-6.6-4.9H1.4v3.1A12 12 0 0 0 12 24z" />
      <path fill="#FBBC05" d="M5.4 14.4a7.2 7.2 0 0 1 0-4.6V6.7H1.4a12 12 0 0 0 0 10.7l4-3z" />
      <path fill="#EA4335" d="M12 4.8c1.8 0 3.3.6 4.6 1.8l3.4-3.4A12 12 0 0 0 1.4 6.7l4 3.1C6.3 6.9 8.9 4.8 12 4.8z" />
    </svg>
  );
}

function AppleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M16.4 12.7c0-2.6 2.1-3.9 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.1 2.5-1.8 3.1-.5 7.6 1.3 10.1.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.3.8c1.4 0 2.3-1.2 3.1-2.5.6-.9 1-1.8 1.3-2.8-3.3-1.3-2.7-4-2.7-4zM14 4.9c.7-.9 1.2-2.1 1.1-3.3-1 0-2.3.7-3.1 1.6-.7.8-1.3 2-1.1 3.2 1.2.1 2.4-.6 3.1-1.5z" />
    </svg>
  );
}

function SpinnerIcon() {
  return (
    <svg className="animate-spin" width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeDasharray="31.4 31.4" />
    </svg>
  );
}
