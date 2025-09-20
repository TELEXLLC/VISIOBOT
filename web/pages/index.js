import { signIn, signOut, useSession } from "next-auth/react";
export default function Home() {
  const { data: session } = useSession();
  return (
    <div>
      <h1>VISIOBOT</h1>
      {session ? (
        <>
          <p>Welcome, {session.user.name}!</p>
          <img src={session.user.image} alt="avatar" />
          <br />
          <a href="/dashboard">Go to Dashboard</a>
          <br />
          <button onClick={() => signOut()}>Sign out</button>
        </>
      ) : (
        <button onClick={() => signIn("discord")}>Login with Discord</button>
      )}
    </div>
  );
}