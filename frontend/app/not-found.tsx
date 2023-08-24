import React from 'react'

type Props = {}

export default function Notfound({ }: Props) {
    return (
        <div className='flex justify-center items-center h-screen'>
            <p className='text-red-600 text-3xl font-mono'>404 Not Found !</p>
        </div>
    )
}