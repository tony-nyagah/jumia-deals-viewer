/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/irlQr0rkoRX
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */

/** Add fonts into your Next.js project:

import { Arimo } from 'next/font/google'
import { Rubik } from 'next/font/google'

arimo({
  subsets: ['latin'],
  display: 'swap',
})

rubik({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
"use client";

import { JSX, SVGProps, useState } from "react";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { Pagination } from "@/components/ui/pagination";

import getDeals from "@/lib/fetchData";

export function DealsViewer() {
  const [currentPage, setCurrentPage] = useState(1);
  const [dealsPerPage] = useState(15);
  const deals = [
    {
      id: 1,
      image: "/placeholder.svg",
      name: "Xiaomi Redmi Note 10 Pro",
      originalPrice: 29999,
      discountedPrice: 22999,
      url: "https://www.jumia.co.ke/xiaomi-redmi-note-10-pro-6.43-120hz-amoled-display-8gb-ram-128gb-rom-64mp-quad-camera-5020mah-battery-graphite-gray-116321.html",
    },
    {
      id: 2,
      image: "/placeholder.svg",
      name: "Samsung Galaxy A52s 5G",
      originalPrice: 39999,
      discountedPrice: 34999,
      url: "https://www.jumia.co.ke/samsung-galaxy-a52s-5g-6.5-120hz-super-amoled-display-8gb-ram-256gb-rom-64mp-quad-camera-4500mah-battery-awesome-black-116320.html",
    },
    {
      id: 3,
      image: "/placeholder.svg",
      name: "Apple iPhone 12 Pro Max",
      originalPrice: 109999,
      discountedPrice: 99999,
      url: "https://www.jumia.co.ke/apple-iphone-12-pro-max-6.7-super-retina-xdr-display-6gb-ram-128gb-rom-12mp-triple-camera-3687mah-battery-pacific-blue-116319.html",
    },
    {
      id: 4,
      image: "/placeholder.svg",
      name: "OPPO Reno6 5G",
      originalPrice: 49999,
      discountedPrice: 44999,
      url: "https://www.jumia.co.ke/oppo-reno6-5g-6.43-90hz-amoled-display-8gb-ram-128gb-rom-64mp-quad-camera-4300mah-battery-stellar-black-116318.html",
    },
    {
      id: 5,
      image: "/placeholder.svg",
      name: "Tecno Camon 18 Premier",
      originalPrice: 29999,
      discountedPrice: 26999,
      url: "https://www.jumia.co.ke/tecno-camon-18-premier-6.7-90hz-amoled-display-8gb-ram-256gb-rom-64mp-quad-camera-4500mah-battery-iris-purple-116317.html",
    },
    {
      id: 6,
      image: "/placeholder.svg",
      name: "OPPO Find X3 Neo",
      originalPrice: 59999,
      discountedPrice: 54999,
      url: "https://www.jumia.co.ke/oppo-find-x3-neo-6.55-90hz-amoled-display-12gb-ram-256gb-rom-50mp-quad-camera-4500mah-battery-stellar-black-116316.html",
    },
    {
      id: 7,
      image: "/placeholder.svg",
      name: "Xiaomi 11T Pro",
      originalPrice: 49999,
      discountedPrice: 44999,
      url: "https://www.jumia.co.ke/xiaomi-11t-pro-6.55-120hz-amoled-display-8gb-ram-256gb-rom-108mp-triple-camera-5000mah-battery-meteorite-gray-116315.html",
    },
    {
      id: 8,
      image: "/placeholder.svg",
      name: "Samsung Galaxy Z Fold3 5G",
      originalPrice: 159999,
      discountedPrice: 149999,
      url: "https://www.jumia.co.ke/samsung-galaxy-z-fold3-5g-7.6-120hz-dynamic-amoled-2x-display-12gb-ram-256gb-rom-12mp-triple-camera-4400mah-battery-phantom-black-116314.html",
    },
    {
      id: 9,
      image: "/placeholder.svg",
      name: "OPPO Reno7 5G",
      originalPrice: 54999,
      discountedPrice: 49999,
      url: "https://www.jumia.co.ke/oppo-reno7-5g-6.43-90hz-amoled-display-8gb-ram-256gb-rom-64mp-triple-camera-4500mah-battery-starlight-black-116313.html",
    },
    {
      id: 10,
      image: "/placeholder.svg",
      name: "Tecno Spark 8 Pro",
      originalPrice: 19999,
      discountedPrice: 16999,
      url: "https://www.jumia.co.ke/tecno-spark-8-pro-6.6-90hz-dot-in-display-8gb-ram-128gb-rom-48mp-quad-camera-5000mah-battery-blue-fusion-116312.html",
    },
  ];

  const dealsJson = getDeals();
  const indexOfLastDeal = currentPage * dealsPerPage;
  const indexOfFirstDeal = indexOfLastDeal - dealsPerPage;
  const currentDeals = deals.slice(indexOfFirstDeal, indexOfLastDeal);
  const totalPages = Math.ceil(deals.length / dealsPerPage);
  const handlePageChange = (pageNumber: number) => {
    setCurrentPage(pageNumber);
  };
  const handleRefresh = () => {
    setCurrentPage(1);
  };

  console.log(dealsJson);

  return (
    <section className="py-12 px-4 md:px-6">
      <div className="container mx-auto max-w-6xl">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-2xl font-bold">Today's Deals</h1>
          <Button variant="outline" onClick={handleRefresh}>
            <RefreshCwIcon className="w-4 h-4 mr-2" />
            Refresh
          </Button>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {currentDeals.map((deal) => (
            <div
              key={deal.id}
              className="bg-background rounded-lg shadow-lg overflow-hidden group"
            >
              <div className="aspect-w-4 aspect-h-3">
                <img
                  src="/placeholder.svg"
                  alt={deal.name}
                  width={400}
                  height={300}
                  className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-300"
                />
              </div>
              <div className="p-4">
                <h3 className="text-lg font-semibold mb-2">{deal.name}</h3>
                <div className="flex items-center gap-2">
                  <span className="text-primary font-bold text-xl">
                    KES {deal.discountedPrice.toLocaleString()}
                  </span>
                  <span className="text-muted-foreground line-through text-sm">
                    KES {deal.originalPrice.toLocaleString()}
                  </span>
                </div>
                <div className="mt-4">
                  <Link
                    href="#"
                    target="_blank"
                    className="inline-flex items-center gap-2 text-primary hover:underline"
                    prefetch={false}
                  >
                    <span>View product</span>
                    <ArrowRightIcon className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="flex justify-center mt-8">
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={handlePageChange}
          />
        </div>
      </div>
    </section>
  );
}

function ArrowRightIcon(
  props: JSX.IntrinsicAttributes & SVGProps<SVGSVGElement>
) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M5 12h14" />
      <path d="m12 5 7 7-7 7" />
    </svg>
  );
}

function RefreshCwIcon(
  props: JSX.IntrinsicAttributes & SVGProps<SVGSVGElement>
) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8" />
      <path d="M21 3v5h-5" />
      <path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16" />
      <path d="M8 16H3v5" />
    </svg>
  );
}