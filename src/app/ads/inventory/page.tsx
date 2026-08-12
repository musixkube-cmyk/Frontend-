"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Placements & Inventory</h1>
        <p className="mt-1 text-sm text-neutral-500">Understand availability and performance across all ad placements.</p>
      </div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <Link
            href="/ads/inventory/feed-audio"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">In-Feed Audio</h3>
            <p className="mt-1 text-xs text-neutral-500">Audio ads between songs in user feeds</p>
          </Link>
          <Link
            href="/ads/inventory/feed-video"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">In-Feed Video</h3>
            <p className="mt-1 text-xs text-neutral-500">Video ads in content feeds</p>
          </Link>
          <Link
            href="/ads/inventory/top-feed"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Top Feed</h3>
            <p className="mt-1 text-xs text-neutral-500">Premium placement at top of feed</p>
          </Link>
          <Link
            href="/ads/inventory/search"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Search Ads</h3>
            <p className="mt-1 text-xs text-neutral-500">Ads in search results</p>
          </Link>
          <Link
            href="/ads/inventory/catalog"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Catalog Ads</h3>
            <p className="mt-1 text-xs text-neutral-500">Product-based catalog placements</p>
          </Link>
          <Link
            href="/ads/inventory/automatic"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Automatic Placements</h3>
            <p className="mt-1 text-xs text-neutral-500">Let the system optimize placement selection</p>
          </Link>

      </div>
    </div>
  );
}
