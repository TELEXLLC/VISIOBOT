import NextAuth from "next-auth";
import DiscordProvider from "next-auth/providers/discord";
export default NextAuth({
  providers: [
    DiscordProvider({
      clientId: process.env.OAUTH2_CLIENT_ID,
      clientSecret: process.env.OAUTH2_CLIENT_SECRET,
    }),
  ],
  session: {
    strategy: "jwt",
  },
});