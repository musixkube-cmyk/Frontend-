"use client";

export default function AnalyticsOverview() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Analytics Overview</h1>
        <p className="mt-1 text-sm text-neutral-500">Diagnose performance across campaigns, ad groups, ads, and audiences.</p>
      </div>

      {/* Breakdown selector */}
      <div className="mb-6 flex gap-2">
        {["Campaign", "Ad Group", "Ad", "Audience", "Creative", "Delivery"].map((view, i) => (
          <button key={view} className={`rounded-lg px-3 py-1.5 text-sm font-medium transition-colors ${i === 0 ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-600 hover:bg-neutral-50"}`}>{view}</button>
        ))}
      </div>

      {/* Metric scorecards */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-6">
        {[
          { label: "Spend", value: "$3,680" },
          { label: "Impressions", value: "142K" },
          { label: "Clicks", value: "1,824" },
          { label: "CTR", value: "1.28%" },
          { label: "CPA", value: "$19.78" },
          { label: "ROAS", value: "3.4x" },
        ].map((m) => (
          <div key={m.label} className="rounded-xl border border-neutral-100 bg-white p-4">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{m.label}</p>
            <p className="mt-1 text-xl font-bold text-neutral-900">{m.value}</p>
          </div>
        ))}
      </div>

      {/* Chart placeholder */}
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Performance trend</h3>
        <div className="flex h-48 items-center justify-center text-sm text-neutral-400">
          Chart renders here — connect to analytics API
        </div>
      </div>
    </div>
  );
}
