import React, { useState } from 'react';

const SidebarLayout = () => {
  const [activeButton, setActiveButton] = useState(0);

  const buttons = [ 
    {
      icon: (
        <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
      )
    },
    {
      icon: (
        <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
        </svg>
      )
    }
  ];

  const handleButtonClick = (index) => {
    setActiveButton(index);
  };

  return (
    
    <aside className="w-20 bg-gray-900 border-r border-gray-200">
          <div className="h-full flex flex-col items-center py-4">
            {/* Logo */}
            <div className="p-2">
              <img src="https://static.vecteezy.com/system/resources/previews/031/391/043/non_2x/ctf-letter-logo-ctf-creative-monogram-initials-letter-logo-concept-ctf-unique-modern-flat-abstract-letter-logo-design-vector.jpg" alt="Logo" className="h-14 w-14" />
            </div>

            {/* Navigation */}
            <nav className="flex-1 w-full px-2 space-y-2 mt-6">
              {buttons.map((button, index) => (
                <button
                  key={index}
                  className={`w-full p-3 flex justify-center rounded-lg ${activeButton === index ? 'bg-indigo-50 text-indigo-600' : 'text-gray-500 hover:bg-gray-50'}`}
                  onClick={() => handleButtonClick(index)}
                >
                  {button.icon}
                </button>
              ))}
            </nav>
          </div>
    </aside>

        
  );
};

export default SidebarLayout;
