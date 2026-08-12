"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

const steps = ["Intent", "Organization", "Business Info", "Account", "Verification", "Invite Members"];

export default function Onboarding() {
  const [step, setStep] = useState(0);
  const router = useRouter();
  const [intent, setIntent] = useState("");
  const [orgType, setOrgType] = useState("");

  return (
    <div className="mx-auto max-w-2xl">
      <div className="mb-8 text-center">
        <img src="/musicosy-orange-logo.webp" alt="Musicosy" className="mx-auto h-10 w-auto object-contain" />
        <h1 className="mt-4 text-2xl font-bold text-neutral-900">Set up your Ad Center</h1>
        <p className="mt-1 text-sm text-neutral-500">Step {step + 1} of {steps.length}</p>
      </div>

      {/* Progress bar */}
      <div className="mb-8 flex gap-1">
        {steps.map((_, i) => (
          <div key={i} className={`h-1 flex-1 rounded-full ${i <= step ? "bg-neutral-900" : "bg-neutral-200"}`} />
        ))}
      </div>

      {/* Step 0: Intent */}
      {step === 0 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">What do you want to do?</h2>
          <div className="space-y-3">
            {["Work with artists", "Grow my business"].map((opt) => (
              <button
                key={opt}
                onClick={() => setIntent(opt)}
                className={`w-full rounded-xl border p-4 text-left text-sm transition-colors ${intent === opt ? "border-neutral-900 bg-neutral-50 font-medium" : "border-neutral-200 hover:border-neutral-300"}`}
              >
                {opt}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step 1: Organization type */}
      {step === 1 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Organization type</h2>
          <div className="space-y-3">
            {["Advertiser", "Agency"].map((opt) => (
              <button
                key={opt}
                onClick={() => setOrgType(opt)}
                className={`w-full rounded-xl border p-4 text-left text-sm transition-colors ${orgType === opt ? "border-neutral-900 bg-neutral-50 font-medium" : "border-neutral-200 hover:border-neutral-300"}`}
              >
                {opt}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step 2: Business info */}
      {step === 2 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Business information</h2>
          <div className="space-y-4">
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Business name</label><input className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Industry</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>Music & Entertainment</option><option>Technology</option><option>Retail</option></select></div>
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Country</label><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Website</label><input placeholder="https://..." className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            </div>
          </div>
        </div>
      )}

      {/* Step 3: Advertiser account */}
      {step === 3 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Advertiser account</h2>
          <div className="space-y-4">
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Account name</label><input className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Time zone</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>America/Chicago</option><option>America/New_York</option><option>America/Los_Angeles</option></select></div>
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Currency</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>USD</option><option>EUR</option><option>GBP</option></select></div>
            </div>
          </div>
        </div>
      )}

      {/* Step 4: Verification */}
      {step === 4 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Business verification</h2>
          <p className="text-sm text-neutral-500 mb-4">Verification enables full ad delivery and payment features.</p>
          <div className="space-y-3">
            <div className="rounded-xl border border-neutral-200 p-4"><h3 className="text-sm font-medium text-neutral-900">Start verification</h3><p className="text-xs text-neutral-500">Submit business documents for review</p></div>
            <div className="rounded-xl border border-neutral-200 p-4"><h3 className="text-sm font-medium text-neutral-900">Creator engagement eligibility</h3><p className="text-xs text-neutral-500">Required for creator collaboration features</p></div>
            <div className="rounded-xl border border-neutral-200 p-4"><h3 className="text-sm font-medium text-neutral-900">Analytics eligibility</h3><p className="text-xs text-neutral-500">Access advanced measurement and insights</p></div>
          </div>
        </div>
      )}

      {/* Step 5: Invite members */}
      {step === 5 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Invite team members</h2>
          <p className="text-sm text-neutral-500 mb-4">Add collaborators to help manage your ad campaigns.</p>
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Email</label><input placeholder="colleague@company.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Role</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>Admin</option><option>Editor</option><option>Viewer</option></select></div>
            </div>
            <button className="text-sm font-medium text-neutral-600">+ Add another member</button>
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="mt-8 flex items-center justify-between">
        <button onClick={() => step > 0 && setStep(step - 1)} className={`text-sm font-medium ${step > 0 ? "text-neutral-700" : "text-neutral-300"}`} disabled={step === 0}>Back</button>
        {step < steps.length - 1 ? (
          <button onClick={() => setStep(step + 1)} className="rounded-lg bg-neutral-900 px-6 py-2.5 text-sm font-medium text-white">Continue</button>
        ) : (
          <button onClick={() => router.push("/ads")} className="rounded-lg bg-neutral-900 px-6 py-2.5 text-sm font-medium text-white">Go to Ad Center</button>
        )}
      </div>
    </div>
  );
}
