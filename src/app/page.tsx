"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { Logo } from "@/components/Logo";

const sections = [
  {
    id: "stream",
    word: "Stream",
    body: "Your favorite songs and podcasts. Follow and discover your favorite creators, build your own playlist, go live with friends who share your taste in music.",
  },
  {
    id: "earn",
    word: "Earn",
    body: "Monetize your audience: streams, downloads, subscribers and merch.",
  },
  {
    id: "publish",
    word: "Publish",
    body: "Your music once. Labels, sync agents, distributors and advertisers looking for your sound and audience.",
  },
  {
    id: "create",
    word: "Create",
    body: "Music and podcasts with studio tools built to help you reach your audience.",
  },
  {
    id: "engage",
    word: "Engage",
    body: "Talk to your listeners and followers, get real-time feedback, and sell merch directly.",
  },
  {
    id: "manage",
    word: "Manage",
    body: "Handle rights, touring, rosters, distribution and social campaigns — all in one place.",
  },
  {
    id: "grow",
    word: "Grow",
    body: "Reach the audience that fits your sound. Partner with artists who share your vision.",
  },
];

export default function Home() {
  const [active, setActive] = useState(0);
  const wordRefs = useRef<(HTMLDivElement | null)[]>([]);

  useEffect(() => {
    let frame = 0;
    const onScroll = () => {
      if (frame) return;
      frame = requestAnimationFrame(() => {
        frame = 0;
        const vh = window.innerHeight;
        let current = 0;
        wordRefs.current.forEach((el, i) => {
          if (!el) return;
          const rect = el.getBoundingClientRect();
          // 0 when entering from the bottom, 1 when parked at its position
          const p = Math.min(Math.max(1 - (rect.top - vh * 0.2) / (vh * 0.8), 0), 1);
          el.style.setProperty("--p", String(p));
          if (p > 0.65) current = i;
        });
        setActive(current);
      });
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      if (frame) cancelAnimationFrame(frame);
    };
  }, []);

  return (
    <div className="relative flex min-h-screen flex-col text-ink-foreground">
      {/* Full-bleed background video */}
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
        <div className="absolute inset-0 bg-ink/50" />
        <div className="absolute inset-0 bg-gradient-to-r from-ink/60 via-ink/30 to-ink/10" />
      </div>

      {/* Top bar */}
      <header className="fixed inset-x-0 top-0 z-30 flex items-center justify-between px-5 py-4 sm:px-10">
        <Logo className="h-8" />
        <div className="flex items-center gap-2">
          <Link
            href="/onboarding"
            className="rounded-full border border-ink-foreground/25 px-4 py-2 text-sm font-medium text-ink-foreground/90 backdrop-blur transition-colors hover:border-primary hover:text-primary"
          >
            Log in
          </Link>
          <Link
            href="/onboarding"
            className="rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-glow"
          >
            Join
          </Link>
        </div>
      </header>

      {/* Far-left rail */}
      <nav
        aria-label="Sections"
        className="fixed left-4 top-1/2 z-30 hidden -translate-y-1/2 flex-col gap-3 sm:flex"
      >
        {sections.map((s, i) => (
          <a
            key={s.id}
            href={`#${s.id}`}
            className={`flex items-baseline gap-1 font-display text-sm uppercase tracking-[0.28em] transition-colors ${
              active === i ? "text-primary" : "text-ink-muted hover:text-ink-foreground"
            }`}
          >
            {s.word}
            <span className="text-primary">+</span>
          </a>
        ))}
      </nav>

      {/* Hero */}
      <section className="relative flex min-h-screen flex-col justify-end px-5 pb-24 sm:px-10 lg:pl-32">
        <h1 className="font-display text-[13vw] font-bold leading-[0.85] tracking-tight sm:text-[9vw]">
          Everything music.
          <span className="block text-primary">One place.</span>
        </h1>
        <p className="mt-6 max-w-md text-lg text-ink-muted">
          Zero gravity, zero gatekeepers. Scroll down.
        </p>
      </section>

      {/* Scrolling block-letter sections */}
      {sections.map((s, i) => (
        <section
          key={s.id}
          id={s.id}
          className="relative flex min-h-screen items-center overflow-hidden px-5 sm:px-10 lg:pl-32"
        >
          <div className="w-full">
            <div
              ref={(el) => {
                wordRefs.current[i] = el;
              }}
              style={{ "--p": 0 } as React.CSSProperties}
              className="[transform:translateX(calc((1_-_var(--p))_*_60vw))] [opacity:calc(0.15_+_var(--p)_*_0.85)] will-change-transform"
            >
              <p className="font-display text-sm uppercase tracking-[0.3em] text-primary">
                0{i + 1}
              </p>
              <h2 className="flex items-baseline gap-2 font-display text-[20vw] font-bold uppercase leading-[0.8] tracking-tighter sm:text-[15vw]">
                {s.word}
                <Link href="/onboarding" className="text-[0.35em] font-semibold normal-case tracking-normal text-primary transition-colors hover:text-primary/80">+</Link>
              </h2>
            </div>
            <p className="mt-8 max-w-lg text-lg leading-relaxed text-ink-muted">{s.body}</p>

          </div>
        </section>
      ))}

      {/* Bottom rail */}
      <footer className="mt-auto border-t border-ink-foreground/10 px-5 py-6 sm:px-10 lg:pl-32">
        <nav aria-label="Bottom rail" className="flex flex-wrap gap-x-4 gap-y-2 text-xs text-ink-muted">
          <a href="/about" className="transition-colors hover:text-ink-foreground">About</a>
          <a href="/get-app" className="transition-colors hover:text-ink-foreground">Get App</a>
          <a href="/help" className="transition-colors hover:text-ink-foreground">Help</a>
          <a href="/terms" className="transition-colors hover:text-ink-foreground">Terms</a>
          <a href="/privacy" className="transition-colors hover:text-ink-foreground">Privacy</a>
          <a href="/cookies" className="transition-colors hover:text-ink-foreground">Cookies</a>
          <a href="/careers" className="transition-colors hover:text-ink-foreground">Careers</a>
          <a href="/ads-business" className="transition-colors hover:text-ink-foreground">Ads & Business</a>
          <a href="/developers" className="transition-colors hover:text-ink-foreground">Developers</a>
          <a href="/news" className="transition-colors hover:text-ink-foreground">News</a>
          <a href="/us-tida" className="transition-colors hover:text-ink-foreground">US TIDA</a>
          <a href="/accessibility" className="transition-colors hover:text-ink-foreground">Accessibility</a>
          <a href="/help-center" className="transition-colors hover:text-ink-foreground">Help Center</a>
        </nav>
        <p className="mt-3 text-xs text-ink-muted">&copy; {new Date().getFullYear()} Musicosy</p>
      </footer>
    </div>
  );
}
