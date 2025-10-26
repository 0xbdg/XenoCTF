import { useState, useEffect } from "react";
import ChallengeCard from "../Components/ChallengeCard.jsx"
import axios from "axios";

export default function ChallengesPage() {
    const [challData, setChallData] = useState([]);
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/test/challenge/")
            .then((response) => {
                setChallData(response.data);
            })
            .catch((err) => {
                console.error(err);
            })
    }, []);
    return (
        <div class="container mx-auto p-6">
            <div class="space-y-8">
                <div>
                    <h2 class="text-2xl font-semibold text-gray-800 mb-4">Web Exploitation</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                        {challData.map((d) => {
                            const data = {
                                chall: d.name,
                                point: d.value,
                                desc: d.message
                            }
                            if (d.category == "web") {
                                return <ChallengeCard key={d.id} {...data} />
                            }
                        })}
                    </div>
                </div>

                <div>
                    <h2 class="text-2xl font-semibold text-gray-800 mb-4">Category 2</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                            <h3 class="text-xl font-medium text-gray-800">Box A</h3>
                            <p class="text-gray-600 mt-2">Description for box A</p>
                        </div>
                        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                            <h3 class="text-xl font-medium text-gray-800">Box B</h3>
                            <p class="text-gray-600 mt-2">Description for box B</p>
                        </div>
                        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                            <h3 class="text-xl font-medium text-gray-800">Box C</h3>
                            <p class="text-gray-600 mt-2">Description for box C</p>
                        </div>
                    </div>
                </div>

                <div>
                    <h2 class="text-2xl font-semibold text-gray-800 mb-4">Category 3</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                            <h3 class="text-xl font-medium text-gray-800">Box X</h3>
                            <p class="text-gray-600 mt-2">Description for box X</p>
                        </div>
                        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                            <h3 class="text-xl font-medium text-gray-800">Box Y</h3>
                            <p class="text-gray-600 mt-2">Description for box Y</p>
                        </div>
                        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                            <h3 class="text-xl font-medium text-gray-800">Box Z</h3>
                            <p class="text-gray-600 mt-2">Description for box Z</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
