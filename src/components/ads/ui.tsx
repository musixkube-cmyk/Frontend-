"use client";

/* ─── MetricCard ─── */
interface MetricCardProps {
  label: string;
  value: string | number;
  delta?: string;
  deltaType?: "positive" | "negative" | "neutral";
  prefix?: string;
}
export function MetricCard({ label, value, delta, deltaType = "neutral", prefix }: MetricCardProps) {
  return (
    <div className="rounded-xl border border-neutral-100 bg-white p-5">
      <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{label}</p>
      <p className="mt-2 text-3xl font-bold text-neutral-900">{prefix}{value}</p>
      {delta && (
        <p className={`mt-1 text-xs font-medium ${deltaType === "positive" ? "text-emerald-600" : deltaType === "negative" ? "text-red-500" : "text-neutral-500"}`}>
          {delta}
        </p>
      )}
    </div>
  );
}

/* ─── StatusBadge ─── */
type Status = "active" | "paused" | "draft" | "completed" | "pending_review" | "rejected" | "in_review";
const statusStyles: Record<Status, string> = {
  active: "bg-emerald-50 text-emerald-700",
  paused: "bg-neutral-100 text-neutral-500",
  draft: "bg-blue-50 text-blue-700",
  completed: "bg-neutral-100 text-neutral-600",
  pending_review: "bg-amber-50 text-amber-700",
  rejected: "bg-red-50 text-red-600",
  in_review: "bg-amber-50 text-amber-700",
};
const statusLabels: Record<Status, string> = {
  active: "Active", paused: "Paused", draft: "Draft", completed: "Completed",
  pending_review: "Pending Review", rejected: "Rejected", in_review: "In Review",
};

interface StatusBadgeProps { status: Status; label?: string; }
export function StatusBadge({ status, label }: StatusBadgeProps) {
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${statusStyles[status] ?? "bg-neutral-100 text-neutral-500"}`}>
      {label ?? statusLabels[status] ?? status}
    </span>
  );
}

/* ─── StatusToggle ─── */
interface StatusToggleProps { active: boolean; onToggle: () => void; }
export function StatusToggle({ active, onToggle }: StatusToggleProps) {
  return (
    <button
      onClick={onToggle}
      className={`relative inline-flex h-5 w-9 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors ${active ? "bg-emerald-500" : "bg-neutral-200"}`}
    >
      <span className={`pointer-events-none inline-block h-4 w-4 rounded-full bg-white shadow transition-transform ${active ? "translate-x-4" : "translate-x-0"}`} />
    </button>
  );
}

/* ─── PageHeader ─── */
interface PageHeaderProps {
  title: string;
  description?: string;
  breadcrumbs?: { label: string; href?: string }[];
  actions?: React.ReactNode;
}
export function PageHeader({ title, description, breadcrumbs, actions }: PageHeaderProps) {
  return (
    <div className="mb-6">
      {breadcrumbs && breadcrumbs.length > 0 && (
        <div className="mb-2 flex items-center gap-1.5 text-sm text-neutral-500">
          {breadcrumbs.map((crumb, i) => (
            <span key={i} className="flex items-center gap-1.5">
              {i > 0 && <span className="text-neutral-300">/</span>}
              {crumb.href ? (
                <a href={crumb.href} className="transition-colors hover:text-neutral-900">{crumb.label}</a>
              ) : (
                <span className={i === breadcrumbs.length - 1 ? "text-neutral-900" : ""}>{crumb.label}</span>
              )}
            </span>
          ))}
        </div>
      )}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">{title}</h1>
          {description && <p className="mt-1 text-sm text-neutral-500">{description}</p>}
        </div>
        {actions && <div className="flex items-center gap-2">{actions}</div>}
      </div>
    </div>
  );
}

/* ─── TabBar ─── */
interface TabBarProps { tabs: string[]; active: number; onChange: (index: number) => void; }
export function TabBar({ tabs, active, onChange }: TabBarProps) {
  return (
    <div className="mb-6 flex gap-1 border-b border-neutral-200">
      {tabs.map((tab, i) => (
        <button
          key={tab}
          onClick={() => onChange(i)}
          className={`px-4 py-2.5 text-sm font-medium transition-colors ${
            i === active ? "border-b-2 border-neutral-900 text-neutral-900" : "text-neutral-500 hover:text-neutral-700"
          }`}
        >
          {tab}
        </button>
      ))}
    </div>
  );
}

/* ─── FilterBar ─── */
interface FilterBarProps {
  searchPlaceholder?: string;
  filters?: { label: string; options: string[] }[];
  onSearch?: (value: string) => void;
}
export function FilterBar({ searchPlaceholder = "Search…", filters = [], onSearch }: FilterBarProps) {
  return (
    <div className="mb-4 flex flex-wrap items-center gap-3">
      <div className="relative flex-1 min-w-[200px]">
        <svg className="absolute left-3 top-1/2 -translate-y-1/2 text-neutral-400" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" />
        </svg>
        <input
          placeholder={searchPlaceholder}
          onChange={(e) => onSearch?.(e.target.value)}
          className="w-full rounded-lg border border-neutral-200 py-2 pl-9 pr-3 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none"
        />
      </div>
      {filters.map((filter) => (
        <select key={filter.label} className="rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
          <option>{filter.label}</option>
          {filter.options.map((opt) => <option key={opt}>{opt}</option>)}
        </select>
      ))}
    </div>
  );
}

/* ─── BulkActionToolbar ─── */
interface BulkActionToolbarProps { selectedCount: number; actions: { label: string; href?: string; onClick?: () => void; variant?: "danger" }[]; }
export function BulkActionToolbar({ selectedCount, actions }: BulkActionToolbarProps) {
  if (selectedCount === 0) return null;
  return (
    <div className="mb-4 flex items-center gap-3 rounded-lg bg-neutral-100 px-4 py-2.5">
      <span className="text-sm font-medium text-neutral-700">{selectedCount} selected</span>
      <div className="flex items-center gap-2">
        {actions.map((action) => (
          <button
            key={action.label}
            onClick={action.onClick}
            className={`rounded-lg px-3 py-1.5 text-sm font-medium transition-colors ${
              action.variant === "danger" ? "text-red-600 hover:bg-red-50" : "text-neutral-700 hover:bg-neutral-200"
            }`}
          >
            {action.label}
          </button>
        ))}
      </div>
    </div>
  );
}

/* ─── EmptyState ─── */
interface EmptyStateProps { title: string; description: string; action?: { label: string; href: string }; }
export function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center">
      <div className="flex h-16 w-16 items-center justify-center rounded-full bg-neutral-100">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" className="text-neutral-400">
          <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z" /><polyline points="13 2 13 9 20 9" />
        </svg>
      </div>
      <h3 className="mt-4 text-sm font-semibold text-neutral-900">{title}</h3>
      <p className="mt-1 max-w-sm text-sm text-neutral-500">{description}</p>
      {action && (
        <a href={action.href} className="mt-4 rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">
          {action.label}
        </a>
      )}
    </div>
  );
}

/* ─── DataTable ─── */
interface Column { key: string; label: string; className?: string; render?: (value: any, row: any) => React.ReactNode; }
interface DataTableProps {
  columns: Column[];
  data: any[];
  selectable?: boolean;
  selected?: Set<string>;
  onToggleSelect?: (id: string) => void;
  onToggleAll?: () => void;
  rowHref?: (row: any) => string;
}
export function DataTable({ columns, data, selectable, selected, onToggleSelect, onToggleAll, rowHref }: DataTableProps) {
  const allSelected = data.length > 0 && selected && data.every((row) => selected.has(row.id));
  return (
    <div className="rounded-xl border border-neutral-100 bg-white overflow-hidden">
      <table className="w-full">
        <thead>
          <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
            {selectable && (
              <th className="w-10 px-4 py-3">
                <input
                  type="checkbox"
                  checked={allSelected}
                  onChange={onToggleAll}
                  className="h-4 w-4 rounded border-neutral-300"
                />
              </th>
            )}
            {columns.map((col) => (
              <th key={col.key} className={`px-4 py-3 ${col.className ?? ""}`}>{col.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.length === 0 ? (
            <tr><td colSpan={columns.length + (selectable ? 1 : 0)} className="py-12 text-center text-sm text-neutral-400">No data</td></tr>
          ) : (
            data.map((row) => {
              const Wrapper = rowHref ? "a" : "div";
              const wrapperProps = rowHref ? { href: rowHref(row) } : {};
              return (
                <tr key={row.id} className="border-b border-neutral-50 text-sm last:border-0 hover:bg-neutral-50/50">
                  {selectable && (
                    <td className="px-4 py-3">
                      <input
                        type="checkbox"
                        checked={selected?.has(row.id) ?? false}
                        onChange={() => onToggleSelect?.(row.id)}
                        className="h-4 w-4 rounded border-neutral-300"
                      />
                    </td>
                  )}
                  {columns.map((col) => (
                    <td key={col.key} className={`px-4 py-3 ${col.className ?? ""}`}>
                      {col.render ? col.render(row[col.key], row) : (
                        <span className="text-neutral-700">{row[col.key]}</span>
                      )}
                    </td>
                  ))}
                </tr>
              );
            })
          )}
        </tbody>
      </table>
    </div>
  );
}

/* ─── ActivityTimeline ─── */
interface ActivityItem { id: string; action: string; user: string; time: string; detail?: string; }
interface ActivityTimelineProps { items: ActivityItem[]; }
export function ActivityTimeline({ items }: ActivityTimelineProps) {
  return (
    <div className="space-y-4">
      {items.map((item, i) => (
        <div key={item.id} className="flex gap-3">
          <div className="flex flex-col items-center">
            <div className="flex h-8 w-8 items-center justify-center rounded-full bg-neutral-100 text-xs font-semibold text-neutral-600">
              {item.user[0]}
            </div>
            {i < items.length - 1 && <div className="flex-1 w-px bg-neutral-200" />}
          </div>
          <div className="flex-1 pb-4">
            <p className="text-sm text-neutral-900"><span className="font-medium">{item.user}</span> {item.action}</p>
            {item.detail && <p className="mt-0.5 text-xs text-neutral-500">{item.detail}</p>}
            <p className="mt-0.5 text-xs text-neutral-400">{item.time}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

/* ─── EstimatePanel ─── */
interface EstimatePanelProps { estimates: { label: string; value: string }[]; deliveryLikelihood?: number; }
export function EstimatePanel({ estimates, deliveryLikelihood }: EstimatePanelProps) {
  return (
    <div className="rounded-xl border border-neutral-100 bg-white p-5">
      <h3 className="text-sm font-semibold text-neutral-900 mb-3">Estimated results</h3>
      <div className="space-y-2.5 text-sm">
        {estimates.map((e) => (
          <div key={e.label} className="flex justify-between">
            <span className="text-neutral-500">{e.label}</span>
            <span className="font-medium text-neutral-900">{e.value}</span>
          </div>
        ))}
      </div>
      {deliveryLikelihood !== undefined && (
        <div className="mt-4">
          <div className="flex justify-between text-xs text-neutral-500 mb-1">
            <span>Delivery likelihood</span>
            <span className="font-medium text-neutral-700">{deliveryLikelihood}%</span>
          </div>
          <div className="h-1.5 rounded-full bg-neutral-100">
            <div className="h-1.5 rounded-full bg-emerald-500" style={{ width: `${deliveryLikelihood}%` }} />
          </div>
        </div>
      )}
    </div>
  );
}

/* ─── PolicyPanel ─── */
interface PolicyIssue { severity: "error" | "warning" | "info"; message: string; }
interface PolicyPanelProps { issues: PolicyIssue[]; }
export function PolicyPanel({ issues }: PolicyPanelProps) {
  if (issues.length === 0) {
    return (
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-2">Policy check</h3>
        <p className="text-sm text-emerald-600">No issues found.</p>
      </div>
    );
  }
  return (
    <div className="rounded-xl border border-neutral-100 bg-white p-5">
      <h3 className="text-sm font-semibold text-neutral-900 mb-3">Policy check</h3>
      <div className="space-y-2">
        {issues.map((issue, i) => (
          <div key={i} className={`flex items-start gap-2 rounded-lg p-2.5 text-sm ${
            issue.severity === "error" ? "bg-red-50 text-red-700" : issue.severity === "warning" ? "bg-amber-50 text-amber-700" : "bg-blue-50 text-blue-700"
          }`}>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="mt-0.5 shrink-0">
              {issue.severity === "error" ? <><circle cx="12" cy="12" r="10" /><line x1="15" y1="9" x2="9" y2="15" /><line x1="9" y1="9" x2="15" y2="15" /></> : <><circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" /></>}
            </svg>
            {issue.message}
          </div>
        ))}
      </div>
    </div>
  );
}

/* ─── CardGrid ─── */
interface CardGridProps { cards: { label: string; description?: string; href: string; icon?: string }[]; }
export function CardGrid({ cards }: CardGridProps) {
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {cards.map((card) => (
        <a
          key={card.label}
          href={card.href}
          className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
        >
          <h3 className="text-sm font-semibold text-neutral-900">{card.label}</h3>
          {card.description && <p className="mt-1 text-xs text-neutral-500">{card.description}</p>}
        </a>
      ))}
    </div>
  );
}

/* ─── FormField ─── */
interface FormFieldProps { label: string; children: React.ReactNode; description?: string; }
export function FormField({ label, children, description }: FormFieldProps) {
  return (
    <div>
      <label className="block text-sm font-medium text-neutral-700 mb-1">{label}</label>
      {children}
      {description && <p className="mt-1 text-xs text-neutral-400">{description}</p>}
    </div>
  );
}

/* ─── Button ─── */
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { variant?: "primary" | "secondary" | "danger" | "ghost"; }
export function Button({ variant = "primary", className = "", ...props }: ButtonProps) {
  const base = "inline-flex items-center justify-center gap-2 rounded-lg px-4 py-2 text-sm font-medium transition-colors disabled:opacity-50";
  const styles: Record<string, string> = {
    primary: "bg-neutral-900 text-white hover:bg-neutral-800",
    secondary: "border border-neutral-200 text-neutral-700 hover:bg-neutral-50",
    danger: "bg-red-600 text-white hover:bg-red-700",
    ghost: "text-neutral-600 hover:bg-neutral-100",
  };
  return <button className={`${base} ${styles[variant]} ${className}`} {...props} />;
}
