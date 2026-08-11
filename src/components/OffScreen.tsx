"use client";

import Link from "next/link";

interface OffScreenProps {
  num: string;
  word: string;
  tagline: string;
}

export function OffScreen({ num, word, tagline }: OffScreenProps) {
  return (
    <div className="flex min-h-screen">
      {/* Left panel — dark, logo upper-left at natural size, tagline below */}
      <div className="flex w-full flex-col px-10 pt-16 sm:w-[55%] sm:px-14 lg:px-20 bg-[#1a1a1a]">
        <Link href="/" className="inline-flex items-start" aria-label="Musicosy home">
          <img
            src="/musicosy-logo.png"
            alt="Musicosy"
            className="w-[180px] sm:w-[240px] lg:w-[300px] object-contain"
          />
        </Link>

        <h1 className="mt-14 font-display text-[7vw] font-bold uppercase leading-[0.9] tracking-tight text-white sm:text-[4vw] lg:text-[3.5vw]">
          {tagline}
        </h1>

        <p className="mt-6 font-display text-sm uppercase tracking-[0.3em] text-[oklch(0.72_0.19_45)]">
          {num} — {word}
        </p>
      </div>

      {/* Right panel — gray bg, white card */}
      <div className="flex w-full items-center justify-center bg-[#f5f5f5] px-6 py-16 sm:w-[45%]">
        <div className="w-full max-w-sm rounded-2xl bg-white p-8 shadow-[0_10px_40px_rgba(0,0,0,0.1)] sm:p-10">
          <h2 className="font-display text-xl font-semibold text-black">
            Join Musicosy
          </h2>
          <p className="mt-2 text-sm text-gray-500">
            {word} starts here. Create your account to get going.
          </p>

          <div className="mt-8 space-y-3">
            <button className="flex w-full items-center justify-center gap-3 rounded-lg bg-black px-4 py-3 text-sm font-medium text-white transition-colors hover:bg-gray-800">
              <svg className="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
              Continue with phone
            </button>
            <button className="flex w-full items-center justify-center gap-3 rounded-lg border border-gray-200 bg-white px-4 py-3 text-sm font-medium text-black transition-colors hover:bg-gray-50">
              <svg className="h-5 w-5" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.07 5.07 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
              Continue with Google
            </button>
            <button className="flex w-full items-center justify-center gap-3 rounded-lg border border-gray-200 bg-white px-4 py-3 text-sm font-medium text-black transition-colors hover:bg-gray-50">
              <svg className="h-5 w-5" viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.17 3.52 7.58 8.7 7.28c1.12.07 1.94.64 2.65.68 1.02-.12 1.88-.64 2.94-.58 1.25.06 2.18.52 2.77 1.37-2.55 1.56-2.18 4.78.24 5.72-.34.91-.82 1.79-1.55 2.47zM12.03 7.2c-.14-2.12 1.58-3.86 3.56-4 .18 2.32-1.76 4.16-3.56 4z"/></svg>
              Continue with Apple
            </button>
          </div>

          <div className="my-6 flex items-center gap-4">
            <div className="h-px flex-1 bg-gray-200" />
            <span className="text-xs text-gray-400">or</span>
            <div className="h-px flex-1 bg-gray-200" />
          </div>

          <div className="space-y-3">
            <input
              type="text"
              placeholder="Email or username"
              className="w-full rounded-lg border border-gray-200 bg-white px-4 py-3 text-sm text-black placeholder:text-gray-400 focus:border-gray-400 focus:outline-none focus:ring-1 focus:ring-gray-400"
            />
            <button className="w-full rounded-lg bg-gray-100 px-4 py-3 text-sm font-medium text-gray-400">
              Continue
            </button>
          </div>

          <p className="mt-6 text-center text-xs text-gray-400">
            By continuing, you agree to our{" "}
            <a href="/terms" className="underline hover:text-black">Terms of Service</a>,{" "}
            <a href="/privacy" className="underline hover:text-black">Privacy Policy</a> and{" "}
            <a href="/cookies" className="underline hover:text-black">Cookie Use</a>.
          </p>
        </div>
      </div>
    </div>
  );
}
