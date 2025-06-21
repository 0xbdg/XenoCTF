import SidebarLayout from "../Components/Sidebar.jsx"

export default function ScoreboardPage(){
    return (
    <div className="bg-gray-700">
      <div className="flex h-screen">
        <SidebarLayout /> 

        {/* Main Content */}
        <main className="flex-1 p-6 bg-gray-800">
          <h1 className="text-2xl font-semibold text-white">Scoreboard</h1> 
          <div className="mt-4 p-6">
            <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="px-6 py-3">Participant</th>
                                <th scope="col" class="px-6 py-3">Flags Captured</th>
                                <th scope="col" class="px-6 py-3">Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">Team Alpha</th>
                                <td class="px-6 py-4">5</td>
                                <td class="px-6 py-4">500</td>
                            </tr>
            
                        </tbody>
                    </table>
            </div>
          </div>
        </main>
      </div>
    </div>

    )
}
