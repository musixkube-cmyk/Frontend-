"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Verification</h1>
        <p className="mt-1 text-sm text-neutral-500">Start or check the status of business verification.</p>
      </div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <Link
            href="#"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Start Verification</h3>
            <p className="mt-1 text-xs text-neutral-500">Begin the business verification process</p>
          </Link>
          <Link
            href="#"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Verification Status</h3>
            <p className="mt-1 text-xs text-neutral-500">Check current verification status</p>
          </Link>
          <Link
            href="#"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Creator Engagement</h3>
            <p className="mt-1 text-xs text-neutral-500">Eligibility for creator engagement features</p>
          </Link>
          <Link
            href="#"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">Creator Payment</h3>
            <p className="mt-1 text-xs text-neutral-500">Eligibility for creator payment features</p>
          </Link>

      </div>
    </div>
  );
}
