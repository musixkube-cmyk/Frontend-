"use client";

import Link from "next/link";
import { useState } from "react";
import { entryBySlug, entries } from "@/lib/entries";

interface OffScreenProps {
  slug: string;
}

export function OffScreen({ slug }: OffScreenProps) {
  const entry = entryBySlug(slug);
  if (!entry) return null;

  const [value, setValue] = useState("");

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
          <button
            type="button"
            className="flex h-14 w-full items-center justify-center gap-3 rounded-full bg-primary font-medium text-primary-foreground transition-opacity hover:opacity-90"
          >
            <PhoneIcon /> Continue with phone
          </button>

          <button
            type="button"
            className="mt-3 flex h-14 w-full items-center justify-center gap-3 rounded-full border border-border bg-background font-medium text-foreground transition-colors hover:bg-secondary"
          >
            <GoogleIcon /> Continue with Google
          </button>

          <button
            type="button"
            className="mt-3 flex h-14 w-full items-center justify-center gap-3 rounded-full border border-border bg-background font-medium text-foreground transition-colors hover:bg-secondary"
          >
            <AppleIcon /> Continue with Apple
          </button>

          <div className="my-6 flex items-center gap-4">
            <span className="h-px flex-1 bg-border" />
            <span className="text-sm text-muted-foreground">or</span>
            <span className="h-px flex-1 bg-border" />
          </div>

          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (value.trim()) window.location.href = "/";
            }}
          >
            <label htmlFor="identifier" className="sr-only">
              Email or username
            </label>
            <input
              id="identifier"
              value={value}
              onChange={(e) => setValue(e.target.value)}
              placeholder="Email or username"
              className="h-14 w-full rounded-xl border border-border bg-background px-4 text-base text-foreground placeholder:text-muted-foreground focus:border-ring focus:outline-none"
            />
            <button
              type="submit"
              disabled={!value.trim()}
              className="mt-4 h-14 w-full rounded-full bg-primary font-medium text-primary-foreground transition-opacity hover:opacity-90 disabled:bg-muted disabled:text-muted-foreground"
            >
              Continue
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
