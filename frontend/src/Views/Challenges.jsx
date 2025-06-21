import SidebarLayout from "../Components/Sidebar.jsx"
import ChallengeCard from "../Components/ChallengeCard.jsx" 

export default function ChallengesPage(){
    return (
    <div className="bg-gray-700">
      <div className="flex h-screen">
        <SidebarLayout /> 

        {/* Main Content */}
        <main className="flex-1 p-6 bg-gray-800">
          <h1 className="text-2xl font-semibold text-white">Challenges</h1> 
          <div className="mt-4 p-6 flex">
            <ChallengeCard />
            <ChallengeCard />
          </div>
        </main>
      </div>
    </div>

    )
}
