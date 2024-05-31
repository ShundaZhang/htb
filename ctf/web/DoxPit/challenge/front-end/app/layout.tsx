import type { Metadata } from "next";
import { Inter } from "next/font/google";

import "bootstrap/dist/css/bootstrap.css";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Doxpit",
  description: "Doxpit is a document sharing and publishing website for text-based information such as dox, code-snippets and other stuff.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="mainPage">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
