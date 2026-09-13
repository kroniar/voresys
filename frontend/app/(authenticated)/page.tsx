export default function OverviewPage() {
  return (
    <div className="max-w-xl">
      <p className="text-sm font-medium text-slate-500">OVERVIEW</p>
      <h1 className="mt-2 text-3xl font-semibold tracking-tight">Welcome to Verosys</h1>
      <section className="mt-8 border-y py-6">
        <p className="text-sm text-slate-500">Organization</p>
        <p className="mt-1 font-medium">Your organization</p>
        <p className="mt-6 text-slate-600">Your SRE control plane is ready.</p>
        <p className="mt-2 text-sm text-slate-500">
          Future operational information will appear here.
        </p>
      </section>
    </div>
  );
}
