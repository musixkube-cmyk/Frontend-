"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Ad Group Detail</h1>
          <p className="mt-1 text-sm text-neutral-500">Configure targeting, placements, budget/bid, analytics, and frequency controls.</p>
        </div>
      </div>
      <div className="mb-6 flex gap-1 border-b border-neutral-200">
        {["Targeting", "Placements", "Budget & Bid", "Analytics", "Frequency Controls"].map((tab, i) => (
          <button key={tab} className={`px-4 py-2.5 text-sm font-medium transition-colors ${i === 0 ? "border-b-2 border-neutral-900 text-neutral-900" : "text-neutral-500 hover:text-neutral-700"}`}>{tab}</button>
        ))}
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Audience targeting</h3>
        <div className="grid gap-4 lg:grid-cols-2">
          <div><label className="block text-sm text-neutral-600 mb-1">Location</label><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
          <div><label className="block text-sm text-neutral-600 mb-1">Age</label><input defaultValue="18-55" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
          <div><label className="block text-sm text-neutral-600 mb-1">Gender</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>All</option><option>Male</option><option>Female</option></select></div>
          <div><label className="block text-sm text-neutral-600 mb-1">Language</label><input defaultValue="English" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
        </div>
      </div>
    </div>
  );
}
