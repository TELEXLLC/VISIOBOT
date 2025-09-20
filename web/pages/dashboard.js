import { useEffect, useState } from "react";
import { useSession, signIn } from "next-auth/react";
export default function Dashboard() {
  const { data: session, status } = useSession();
  const [guilds, setGuilds] = useState([]);
  useEffect(() => {
    if (status === "authenticated") {
      fetch(process.env.NEXT_PUBLIC_API_URL + "/server-info")
        .then(res => res.json())
        .then(data => setGuilds(data.guilds || []));
    }
  }, [status]);
  if (status === "loading") return <p>Loading...</p>;
  if (status !== "authenticated")
    return <button onClick={() => signIn("discord")}>Login with Discord</button>;
  return (
    <div>
      <h1>Server Info</h1>
      {guilds.map(g => (
        <div key={g.id} style={{border:"1px solid #ccc",margin:"12px",padding:"8px",borderRadius:"6px"}}>
          <h2>{g.name}</h2>
          <p>Members: {g.member_count}</p>
          {g.icon_url && <img src={g.icon_url} alt="icon" width={64} />}
        </div>
      ))}
    </div>
  );
}