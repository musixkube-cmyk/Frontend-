"use client";

import Link from "next/link";
import { Logo } from "@/components/Logo";

interface OffScreenProps {
  /** The section number, e.g. "01" */
  num: string;
  /** The section word, e.g. "Stream" */
  word: string;
  /** The tagline in large text, e.g. "YOUR SOUND FIRST" */
  tagline: string;
}

export function OffScreen({ num, word, tagline }: OffScreenProps) {
  return (
    <div className="flex min-h-screen">
      {/* Left panel — dark branding */}
      <div className="flex w-full flex-col justify-center bg-ink px-8 py-16 sm:w-1/2 sm:px-12 lg:px-16">
        <Link href="/" className="mb-12 inline-flex items-center" aria-label="Musicosy home">
          <img
            src="/musicosy-logo.png"
            alt="Musicosy"
            className="h-24 w-auto object-contain sm:h-32 lg:h-40"
          />
        </Link>

        <h1 className="font-display text-[10vw] font-bold uppercase leading-[0.85] tracking-tight text-ink-foreground sm:text-[5vw] lg:text-[4vw]">
          {tagline}
        </h1>

        <p className="mt-8 font-display text-sm uppercase tracking-[0.3em] text-primary">
          {num} — {word}
        </p>
      </div>

      {/* Right panel — white card area */}
      <div className="flex w-full items-center justify-center bg-background px-6 py-16 sm:w-1/2">
        <div className="w-full max-w-sm rounded-2xl bg-card p-8 shadow-lift sm:p-10">
          <h2 className="font-display text-xl font-semibold text-card-foreground">
            Join Musicosy
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            {word} starts here. Create your account to get going.
          </p>

          <div className="mt-8 space-y-3">
            <button className="flex w-full items-center justify-center gap-3 rounded-lg border border-border bg-background px-4 py-3 text-sm font-medium text-foreground transition-colors hover:bg-accent">
              <svg className="h-5 w-5" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.07 5.07 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
              Continue with Google
            </button>
            <button className="flex w-full items-center justify-center gap-3 rounded-lg border border-border bg-background px-4 py-3 text-sm font-medium text-foreground transition-colors hover:bg-accent">
              <svg className="h-5 w-5" viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.17 3.52 7.58 8.7 7.28c1.12.07 1.94.64 2.65.68 1.02-.12 1.88-.64 2.94-.58 1.25.06 2.18.52 2.77 1.37-2.55 1.56-2.18 4.78.24 5.72-.34.91-.82 1.79-1.55 2.47zM12.03 7.2c-.14-2.12 1.58-3.86 3.56-4 .18 2.32-1.76 4.16-3.56 4z"/></svg>
              Continue with Apple
            </button>
          </div>

          <div className="my-6 flex items-center gap-4">
            <div className="h-px flex-1 bg-border" />
            <span className="text-xs text-muted-foreground">or</span>
            <div className="h-px flex-1 bg-border" />
          </div>

          <div className="space-y-3">
            <input
              type="text"
              placeholder="Email or username"
              className="w-full rounded-lg border border-border bg-background px-4 py-3 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
            />
            <button className="w-full rounded-lg bg-primary px-4 py-3 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90">
              Continue
            </button>
          </div>

          <p className="mt-6 text-center text-xs text-muted-foreground">
            By continuing, you agree to our{" "}
            <a href="/terms" className="underline hover:text-foreground">Terms</a>{" "}
            and{" "}
            <a href="/privacy" className="underline hover:text-foreground">Privacy Policy</a>.
          </p>
        </div>
      </div>
    </div>
  );
}
