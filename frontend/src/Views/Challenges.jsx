import ChallengeCard from "../Components/ChallengeCard.jsx" 

export default function ChallengesPage(){
    return (
        <div class="container mx-auto p-6">
            <div class="space-y-8">
                <div>
                    <h2 class="text-2xl font-semibold text-gray-800 mb-4">Category 1</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                        <ChallengeCard chall="Test" point="200" desc="lorem ipsum dolor sit amet" /> 
                        <ChallengeCard />  
                        <ChallengeCard /> 
                        <ChallengeCard />  
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

// <div className="bg-gray-700">
//      <div className="flex h-screen">
//        <SidebarLayout /> 
// 
//        <main className="flex-1 p-6 bg-gray-800">
//          <h1 className="text-2xl font-semibold text-white">Challenges</h1> 
//          <div className="mt-4 p-6 flex">
//            <ChallengeCard />
//            <ChallengeCard />
//          </div>
//        </main>
//      </div>
//    </div>
