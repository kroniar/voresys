export const saveSession = (access: string, refresh: string) => { localStorage.setItem("verosys_access_token", access); localStorage.setItem("verosys_refresh_token", refresh); };
export const clearSession = () => { localStorage.removeItem("verosys_access_token"); localStorage.removeItem("verosys_refresh_token"); };
