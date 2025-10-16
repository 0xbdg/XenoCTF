import { useState } from 'react';

const ChallengeCard = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [flag, setFlag] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Flag submitted: ${flag}`);
    setIsOpen(false);
  };

  return (
    <> 
        <button onClick={() => setIsOpen(true)} class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <h3 class="text-xl font-medium text-white">Box 1</h3>
            <p class="text-white mt-2">Description for box 1</p>
        </button> 

      {/* Modal */}
      {isOpen && (
        <div 
          className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-70"
          onClick={() => setIsOpen(false)}
        >
          <div 
            className="relative bg-gray-800 rounded-lg shadow-lg border border-gray-700 w-full max-w-2xl mx-4"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between p-4 md:p-5 border-b rounded-t border-gray-700">
              <h3 className="text-xl font-semibold text-white">
                SQL Injection Challenge
              </h3>
              <button 
                type="button" 
                className="text-gray-400 bg-transparent hover:bg-gray-600 hover:text-white rounded-lg text-sm w-8 h-8"
                onClick={() => setIsOpen(false)}
              >
                <svg className="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                  <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                </svg>
                <span className="sr-only">Close modal</span>
              </button>
            </div>
            <div className="p-4 md:p-5 space-y-4">
              <p className="text-base leading-relaxed text-gray-300">
                <strong>Objective:</strong> Bypass authentication to obtain the flag using SQL injection techniques.
              </p>
              <div className="bg-gray-900 p-4 rounded">
                <p className="text-yellow-400 font-mono text-sm">
                  Hint: Try using a single quote in the username field to test for SQL injection vulnerabilities.
                </p>
              </div>
              <form className="space-y-4" onSubmit={handleSubmit}>
                <div>
                  <label htmlFor="flag" className="block mb-2 text-sm font-medium text-white">
                    Enter Flag
                  </label>
                  <input 
                    type="text" 
                    id="flag" 
                    value={flag}
                    onChange={(e) => setFlag(e.target.value)}
                    className="bg-gray-700 border border-gray-600 text-white text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" 
                    placeholder="CTF{...}" 
                    required
                  />
                </div>
                <div className="flex items-center p-4 md:p-5 border-t border-gray-700 rounded-b">
                  <button 
                    type="submit" 
                    className="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                  >
                    Submit Flag
                  </button>
                  <button 
                    type="button" 
                    className="py-2.5 px-5 ms-3 text-sm font-medium text-white focus:outline-none bg-gray-700 rounded-lg border border-gray-600 hover:bg-gray-600"
                    onClick={() => setFlag('')}
                  >
                    Reset
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default ChallengeCard;
