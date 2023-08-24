"use client"
import Link from 'next/link'
import { motion } from "framer-motion"

export default function Home() {
  return (
    <main>
      <motion.div
        initial={{ opacity: 0, scale: 0.5 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
      >
        <div className="h-screen flex justify-center items-center flex-col font-mono duration-300">
          <h1 className='text-2xl mb-3'>Welcome</h1>
          <div className=''>
            <Link className=' hover:underline text-orange-500' href="/register">Start here.</Link>
          </div>
        </div>
      </motion.div>


    </main>
  )
}
