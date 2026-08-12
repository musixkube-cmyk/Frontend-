"use client";

export default function BillingOverview() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Billing Overview</h1>
        <p className="mt-1 text-sm text-neutral-500">Manage payment, invoices, and billing identity.</p>
      </div>
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Account balance", value: "$4,320" },
          { label: "Current spend", value: "$3,680" },
          { label: "Next invoice", value: "Aug 15, 2026" },
          { label: "Payment method", value: "Visa ····4242" },
        ].map((kpi) => (
          <div key={kpi.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{kpi.label}</p>
            <p className="mt-2 text-2xl font-bold text-neutral-900">{kpi.value}</p>
          </div>
        ))}
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Recent transactions</h3>
        <div className="flex h-32 items-center justify-center text-sm text-neutral-400">Transaction history loads here</div>
      </div>
    </div>
  );
}
