export function PlaceholderPage({ title }: { title: string }) {
  return (
    <div>
      <p className="text-sm font-medium text-slate-500">VEROSYS</p>
      <h1 className="mt-2 text-3xl font-semibold tracking-tight">{title}</h1>
      <p className="mt-4 text-slate-600">This area is planned for a future Verosys capability.</p>
    </div>
  );
}
