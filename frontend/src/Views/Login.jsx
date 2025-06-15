export default function LoginPage(){
    return (
       <div className="bg-black text-green-400 min-h-screen flex items-center justify-center p-4">
            <div className="w-full max-w-md">
                <div className="bg-gray-900 border border-green-500 rounded-lg shadow-lg overflow-hidden">
                    {/* Terminal Header */}
                    <div className="bg-gray-800 px-4 py-3 flex items-center border-b border-green-500">
                        <div className="flex space-x-2 mr-4">
                            <div className="w-3 h-3 rounded-full bg-red-500" />
                            <div className="w-3 h-3 rounded-full bg-yellow-500" />
                            <div className="w-3 h-3 rounded-full bg-green-500" />
                        </div>
                        <div className="text-sm text-green-400">login@terminal:~</div>
                    </div>
                    {/* Terminal Body */}
                    <div className="p-6 space-y-6">
                        <div className="space-y-2">
                            <div className="text-green-500">Terminal Login System v1.0</div>
                                <div className="text-gray-400">--------------------------------</div>
                            </div>
                                <form className="space-y-4">
                                    <div>
                                        <label htmlFor="username" className="block text-green-400 mb-1">Username:</label>
                                        <div className="flex items-center terminal-input">
                                            <input
                                                type="text"
                                                id="username"
                                                className="flex-1 bg-black text-green-400 border-b border-green-500 focus:outline-none focus:border-green-300 px-2 py-1"
                                                autoComplete="off"
                                                autoCorrect="off"
                                                autoCapitalize="none"
                                                spellCheck="false"
                                            />
                                        </div>
                                    </div>
                                    <div>
                                        <label htmlFor="password" className="block text-green-400 mb-1">Password:</label>
                                        <div className="flex items-center terminal-input">
                                            <input
                                                type="password"
                                                id="password"
                                                className="flex-1 bg-black text-green-400 border-b border-green-500 focus:outline-none focus:border-green-300 px-2 py-1"
                                            />
                                        </div>
                                    </div>
                                    <div className="flex items-center justify-between pt-4">
                                        <button
                                            type="submit"
                                            className="bg-green-600 hover:bg-green-700 text-black font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 transition-colors">
                                            LOGIN
                                        </button>
                                        <div className="text-xs text-gray-500 blinking-cursor">ready</div>
                                    </div>
                                </form>
                                <div className="text-xs text-gray-500 pt-4 border-t border-gray-700">
                                    <p>System: Secure terminal access only</p>
                                    <p>Unauthorized access prohibited</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
    )
}
