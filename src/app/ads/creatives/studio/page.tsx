"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Creative Studio</h1>
        <p className="mt-1 text-sm text-neutral-500">Build reusable ad creative. Upload, compose, preview, and generate with AI.</p>
      </div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <Link
            href="/ads/creatives/audio"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Audio Upload</h3>
            <p className="mt-1 text-xs text-neutral-500">Upload and manage audio ad files</p>
          </Link>
          <Link
            href="/ads/creatives/companion"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Companion Images</h3>
            <p className="mt-1 text-xs text-neutral-500">Upload companion visuals for audio ads</p>
          </Link>
          <Link
            href="/ads/creatives/logo"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Logo Manager</h3>
            <p className="mt-1 text-xs text-neutral-500">Upload and manage brand logos</p>
          </Link>
          <Link
            href="/ads/creatives/cta"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">CTA Builder</h3>
            <p className="mt-1 text-xs text-neutral-500">Configure call-to-action buttons</p>
          </Link>
          <Link
            href="/ads/creatives/destination"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Destination URLs</h3>
            <p className="mt-1 text-xs text-neutral-500">Set and validate landing page URLs</p>
          </Link>
          <Link
            href="/ads/creatives/preview"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Ad Preview</h3>
            <p className="mt-1 text-xs text-neutral-500">Preview your ad across placements</p>
          </Link>
          <Link
            href="/ads/creatives/ai"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">AI Generator</h3>
            <p className="mt-1 text-xs text-neutral-500">Generate creative with AI tools</p>
          </Link>
          <Link
            href="/ads/creatives/overlay"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Overlay Manager</h3>
            <p className="mt-1 text-xs text-neutral-500">Manage ad overlays and stickers</p>
          </Link>

      </div>
    </div>
  );
}
