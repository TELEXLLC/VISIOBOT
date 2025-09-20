import React from "react";

export default function Home() {
  const deployOne = process.env.NEXT_PUBLIC_DEPLOYMENT_ONE;
  const deployTwo = process.env.NEXT_PUBLIC_DEPLOYMENT_TWO;
  const deployThree = process.env.NEXT_PUBLIC_DEPLOYMENT_THREE;

  return (
    <main>
      <h1>Welcome to VisioBot</h1>
      <section style={{ margin: "2rem 0", padding: "1rem", background: "#f5f5f5", borderRadius: "8px" }}>
        <h2>Vercel Deploy Hooks</h2>
        <ul>
          <li>
            <a href={deployOne} target="_blank" rel="noopener noreferrer">
              Deploy Hook 1
            </a>
          </li>
          <li>
            <a href={deployTwo} target="_blank" rel="noopener noreferrer">
              Deploy Hook 2
            </a>
          </li>
          <li>
            <a href={deployThree} target="_blank" rel="noopener noreferrer">
              Deploy Hook 3
            </a>
          </li>
        </ul>
      </section>
      {/* ...rest of your homepage */}
    </main>
  );
}
