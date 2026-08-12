"use client";

import { useState } from "react";
import Link from "next/link";
import { Button, FormField, EstimatePanel, PolicyPanel } from "@/components/ads/ui";

const steps = ["Objective", "Campaign", "Ad Group", "Ad", "Review"];

const objectiveTree = [
  { category: "Awareness", items: ["Reach", "Video Views"] },
  { category: "Consideration", items: ["Traffic", "Community Interaction", "Brand Consideration", "Music Streams"] },
  { category: "Conversion", items: ["App Promotion", "Lead Generation", "Sales"] },
];

export default function CreateCampaign() {
  const [step, setStep] = useState(0);
  const [objective, setObjective] = useState("");
  const [objectiveCategory, setObjectiveCategory] = useState("");
  const [campaignName, setCampaignName] = useState("");
  const [specialCategory, setSpecialCategory] = useState("None");
  const [splitTest, setSplitTest] = useState(false);
  const [budgetType, setBudgetType] = useState<"daily" | "weekly" | "monthly" | "lifetime">("daily");
  const [budgetAmount, setBudgetAmount] = useState("50");
  const [budgetOwnership, setBudgetOwnership] = useState<"campaign" | "ad_group">("campaign");
  const [deliveryType, setDeliveryType] = useState<"standard" | "accelerated" | "scheduled">("standard");
  const [budgetCommitment, setBudgetCommitment] = useState(false);

  function selectObjective(cat: string, item: string) {
    setObjectiveCategory(cat);
    setObjective(item);
  }

  return (
    <div>
      {/* Stepper */}
      <div className="mb-8 flex items-center gap-2">
        {steps.map((s, i) => (
          <div key={s} className="flex items-center gap-2">
            <button onClick={() => i <= step && setStep(i)} className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold transition-colors ${i < step ? "bg-neutral-900 text-white" : i === step ? "border-2 border-neutral-900 text-neutral-900" : "border border-neutral-300 text-neutral-400"}`}>
              {i < step ? "✓" : i + 1}
            </button>
            <span className={`text-sm ${i === step ? "font-medium text-neutral-900" : "text-neutral-400"}`}>{s}</span>
            {i < steps.length - 1 && <div className="mx-2 h-px w-8 bg-neutral-200" />}
          </div>
        ))}
      </div>

      <div className="flex gap-6">
        <div className="flex-1">

          {/* ─── Step 1: Objective ─── */}
          {step === 0 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Choose an objective</h2>
              <p className="text-sm text-neutral-500 mb-6">Your objective determines how your ads are optimized and delivered.</p>
              <div className="space-y-6">
                {objectiveTree.map((cat) => (
                  <div key={cat.category}>
                    <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">{cat.category}</h3>
                    <div className="grid grid-cols-2 gap-3">
                      {cat.items.map((item) => (
                        <button key={item} onClick={() => selectObjective(cat.category, item)} className={`rounded-xl border p-4 text-left text-sm transition-colors ${objective === item ? "border-neutral-900 bg-neutral-50 font-medium text-neutral-900" : "border-neutral-200 text-neutral-700 hover:border-neutral-300"}`}>
                          {item}
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* ─── Step 2: Campaign ─── */}
          {step === 1 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Campaign settings</h2>
              <p className="text-sm text-neutral-500 mb-6">Name your campaign, set special categories, and configure budget.</p>
              <div className="space-y-5">
                <FormField label="Campaign name"><input value={campaignName} onChange={(e) => setCampaignName(e.target.value)} placeholder="e.g. Summer Launch 2026" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" /></FormField>

                <FormField label="Special ad category" description="Required for housing, credit, employment, or political ads">
                  <select value={specialCategory} onChange={(e) => setSpecialCategory(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>None</option><option>Housing</option><option>Credit</option><option>Employment</option><option>Politics</option></select>
                </FormField>

                <div className="flex items-center gap-3">
                  <input type="checkbox" checked={splitTest} onChange={(e) => setSplitTest(e.target.checked)} className="h-4 w-4 rounded border-neutral-300" />
                  <label className="text-sm text-neutral-700">Enable split test (A/B test)</label>
                </div>

                <FormField label="Budget ownership">
                  <div className="flex gap-2">
                    <button onClick={() => setBudgetOwnership("campaign")} className={`rounded-lg px-4 py-2 text-sm font-medium ${budgetOwnership === "campaign" ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>Campaign budget optimization</button>
                    <button onClick={() => setBudgetOwnership("ad_group")} className={`rounded-lg px-4 py-2 text-sm font-medium ${budgetOwnership === "ad_group" ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>Ad group budget</button>
                  </div>
                </FormField>

                <FormField label="Budget cadence">
                  <div className="flex gap-2">
                    {(["daily", "weekly", "monthly", "lifetime"] as const).map((t) => (
                      <button key={t} onClick={() => setBudgetType(t)} className={`rounded-lg px-3 py-2 text-sm font-medium capitalize ${budgetType === t ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>{t}</button>
                    ))}
                  </div>
                </FormField>

                <FormField label={`${budgetType.charAt(0).toUpperCase() + budgetType.slice(1)} budget`}>
                  <div className="relative"><span className="absolute left-3 top-1/2 -translate-y-1/2 text-sm text-neutral-400">$</span><input value={budgetAmount} onChange={(e) => setBudgetAmount(e.target.value)} type="number" className="w-full rounded-lg border border-neutral-200 py-2.5 pl-7 pr-3 text-sm text-neutral-900" /></div>
                </FormField>

                <div className="flex items-center gap-3">
                  <input type="checkbox" checked={budgetCommitment} onChange={(e) => setBudgetCommitment(e.target.checked)} className="h-4 w-4 rounded border-neutral-300" />
                  <label className="text-sm text-neutral-700">Budget commitment (spend full budget each period)</label>
                </div>

                <FormField label="Delivery type">
                  <select value={deliveryType} onChange={(e) => setDeliveryType(e.target.value as any)} className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900">
                    <option value="standard">Standard (evenly throughout the day)</option>
                    <option value="accelerated">Accelerated (spend budget as fast as possible)</option>
                    <option value="scheduled">Scheduled (specific days and hours)</option>
                  </select>
                </FormField>
              </div>
            </div>
          )}

          {/* ─── Step 3: Ad Group ─── */}
          {step === 2 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Ad group configuration</h2>
              <p className="text-sm text-neutral-500 mb-6">Define audience, placements, optimization, and brand safety.</p>
              <div className="space-y-5">
                <FormField label="Ad group name"><input defaultValue="Ad Group 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></FormField>

                <div className="rounded-xl border border-neutral-100 bg-neutral-50/50 p-4">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Audience</h3>
                  <div className="grid gap-4 lg:grid-cols-2">
                    <FormField label="Locations"><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                    <FormField label="Age range"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>18–55</option><option>18–24</option><option>25–34</option><option>35–54</option><option>55+</option></select></FormField>
                    <FormField label="Gender"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>All</option><option>Male</option><option>Female</option></select></FormField>
                    <FormField label="Language"><input defaultValue="English" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                    <FormField label="Music behavior"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>All behaviors</option><option>Active streamers</option><option>Playlist curators</option></select></FormField>
                    <FormField label="Artist affinity"><input placeholder="e.g. Drake, The Weeknd" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                  </div>
                  <div className="mt-3 flex gap-2">
                    <Button variant="secondary" className="text-xs">Add custom audience</Button>
                    <Button variant="secondary" className="text-xs">Add exclusion</Button>
                  </div>
                </div>

                <div className="rounded-xl border border-neutral-100 bg-neutral-50/50 p-4">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Placements</h3>
                  <div className="flex flex-wrap gap-2">
                    {["Automatic placements", "In-Feed Audio", "In-Feed Video", "Top Feed", "Search Ads", "Catalog Ads"].map((p, i) => (
                      <button key={p} className={`rounded-lg border px-3 py-1.5 text-xs font-medium transition-colors ${i === 0 ? "border-neutral-900 bg-neutral-50 text-neutral-900" : "border-neutral-200 text-neutral-600 hover:border-neutral-300"}`}>{p}</button>
                    ))}
                  </div>
                </div>

                <div className="rounded-xl border border-neutral-100 bg-neutral-50/50 p-4">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Optimization & bidding</h3>
                  <div className="grid gap-4 lg:grid-cols-2">
                    <FormField label="Optimization goal"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Maximize clicks</option><option>Maximize conversions</option><option>Maximize reach</option><option>Maximize impression delivery</option></select></FormField>
                    <FormField label="Bid strategy"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Lowest cost (auto)</option><option>Cost cap</option><option>Target cost</option><option>Bid cap</option></select></FormField>
                  </div>
                </div>

                <div className="rounded-xl border border-neutral-100 bg-neutral-50/50 p-4">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Frequency capping</h3>
                  <div className="grid gap-4 lg:grid-cols-3">
                    <FormField label="Frequency"><input defaultValue="3" type="number" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                    <FormField label="Period"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Per day</option><option>Per week</option><option>Per month</option></select></FormField>
                    <FormField label="Placement level"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Ad group</option><option>Campaign</option></select></FormField>
                  </div>
                </div>

                <div className="rounded-xl border border-neutral-100 bg-neutral-50/50 p-4">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Brand safety & suitability</h3>
                  <div className="grid gap-4 lg:grid-cols-2">
                    <FormField label="Inventory filter"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Standard</option><option>Limited</option><option>Full</option></select></FormField>
                    <FormField label="Suitability"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Standard</option><option>Conservative</option><option>Liberal</option></select></FormField>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* ─── Step 4: Ad ─── */}
          {step === 3 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Ad creative</h2>
              <p className="text-sm text-neutral-500 mb-6">Choose or create your ad creative, set CTA, destination, and tracking.</p>
              <div className="space-y-5">
                <FormField label="Ad name"><input defaultValue="Ad 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></FormField>

                <FormField label="Audio">
                  <div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-8 text-sm text-neutral-400">
                    <div className="text-center">
                      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="mx-auto mb-2 text-neutral-300"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /><polyline points="17 8 12 3 7 8" /><line x1="12" y1="3" x2="12" y2="15" /></svg>
                      Drag audio file or click to upload
                    </div>
                  </div>
                </FormField>

                <FormField label="Companion image (1200×628)">
                  <div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-8 text-sm text-neutral-400">Upload companion image</div>
                </FormField>

                <div className="grid gap-4 lg:grid-cols-2">
                  <FormField label="Logo"><div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-6 text-sm text-neutral-400">Upload logo (200×200)</div></FormField>
                  <FormField label="Overlay / sticker"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>None</option><option>Shop now sticker</option><option>Download sticker</option></select></FormField>
                </div>

                <div className="grid gap-4 lg:grid-cols-2">
                  <FormField label="CTA"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>Learn More</option><option>Shop Now</option><option>Listen Now</option><option>Download</option><option>Sign Up</option><option>Get Quote</option></select></FormField>
                  <FormField label="Destination URL"><input placeholder="https://..." className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></FormField>
                </div>

                <div className="rounded-xl border border-neutral-100 bg-neutral-50/50 p-4">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Tracking & measurement</h3>
                  <div className="grid gap-4 lg:grid-cols-2">
                    <FormField label="Impression tracker"><input placeholder="URL for impression pixel" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                    <FormField label="Click tracker"><input placeholder="URL for click tracking" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                    <FormField label="UTM source"><input defaultValue="musicosy_ads" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                    <FormField label="UTM medium"><input defaultValue="cpc" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></FormField>
                  </div>
                </div>

                <div className="rounded-xl border border-neutral-100 bg-white p-6">
                  <h3 className="text-sm font-semibold text-neutral-900 mb-3">Live preview</h3>
                  <div className="flex h-48 items-center justify-center rounded-lg bg-neutral-100 text-sm text-neutral-400">Ad preview renders here</div>
                </div>
              </div>
            </div>
          )}

          {/* ─── Step 5: Review ─── */}
          {step === 4 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Review & publish</h2>
              <p className="text-sm text-neutral-500 mb-6">Confirm your configuration before publishing.</p>
              <div className="space-y-4">
                <div className="rounded-xl border border-neutral-100 bg-white p-5">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">Objective</h3>
                  <p className="text-sm text-neutral-900">{objectiveCategory}: <span className="font-medium">{objective || "Not selected"}</span></p>
                </div>
                <div className="rounded-xl border border-neutral-100 bg-white p-5">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">Campaign</h3>
                  <div className="grid grid-cols-2 gap-y-2 text-sm">
                    <span className="text-neutral-500">Name</span><span className="text-neutral-900 font-medium">{campaignName || "Untitled"}</span>
                    <span className="text-neutral-500">Special category</span><span className="text-neutral-900">{specialCategory}</span>
                    <span className="text-neutral-500">Budget</span><span className="text-neutral-900 font-medium">${budgetAmount}/{budgetType}</span>
                    <span className="text-neutral-500">Ownership</span><span className="text-neutral-900">{budgetOwnership === "campaign" ? "CBO" : "Ad group"}</span>
                    <span className="text-neutral-500">Delivery</span><span className="text-neutral-900 capitalize">{deliveryType}</span>
                    <span className="text-neutral-500">Split test</span><span className="text-neutral-900">{splitTest ? "Yes" : "No"}</span>
                  </div>
                </div>
                <PolicyPanel issues={[]} />
              </div>
            </div>
          )}
        </div>

        {/* Right context panel */}
        {step >= 1 && (
          <div className="hidden w-72 shrink-0 lg:block space-y-4">
            <EstimatePanel estimates={[
              { label: "Reach", value: "~24K" },
              { label: "Impressions", value: "~42K" },
              { label: "Clicks", value: "~520" },
              { label: "CPA", value: "~$9.60" },
              { label: "ROAS", value: "~3.2x" },
            ]} deliveryLikelihood={87} />
            {step >= 2 && (
              <PolicyPanel issues={[]} />
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="mt-8 flex items-center justify-between border-t border-neutral-200 pt-4">
        <button onClick={() => step > 0 && setStep(step - 1)} className={`text-sm font-medium ${step > 0 ? "text-neutral-700" : "text-neutral-300"}`} disabled={step === 0}>Back</button>
        <div className="flex gap-3">
          <Button variant="secondary">Save draft</Button>
          {step < 4 ? (
            <Button onClick={() => setStep(step + 1)}>Continue</Button>
          ) : (
            <Button>Publish</Button>
          )}
        </div>
      </div>
    </div>
  );
}
