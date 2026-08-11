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
    <div className="relative flex min-h-screen flex-col items-center justify-center text-ink-foreground">
      {/* Full-bleed background video — crossfade loop */}
      <div className="fixed inset-0 -z-10">
        <video
          className="h-full w-full object-cover"
          src="/astronaut.mp4"
          autoPlay
          muted
          loop
          playsInline
          aria-hidden="true"
        />
        <div className="absolute inset-0 bg-ink/60" />
        <div className="absolute inset-0 bg-gradient-to-r from-ink/70 via-ink/40 to-ink/15" />
      </div>

      {/* Content */}
      <div className="relative z-10 flex w-full max-w-4xl flex-col items-center px-6 py-16 text-center">
        {/* Large logo */}
        <Logo className="h-24 sm:h-32 lg:h-40" />

        {/* Tagline */}
        <h1 className="mt-12 font-display text-[8vw] font-bold uppercase leading-[0.9] tracking-tight text-ink-foreground sm:text-[6vw] lg:text-[5vw]">
          {tagline}
        </h1>

        {/* Section number + word */}
        <p className="mt-8 font-display text-sm uppercase tracking-[0.3em] text-primary">
          {num} — {word}
        </p>

        {/* Back to home */}
        <Link
          href="/"
          className="mt-12 inline-flex items-center gap-2 rounded-full border border-ink-foreground/25 px-6 py-3 text-sm font-medium text-ink-foreground/90 backdrop-blur transition-colors hover:border-primary hover:text-primary"
        >
          ← Home
        </Link>
      </div>
    </div>
  );
}
