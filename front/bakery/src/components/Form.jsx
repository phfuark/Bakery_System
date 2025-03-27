export function Form() {
    return (
        <div className="p-6 bg-[#2D080A] text-[#FFCDBC] rounded-lg shadow-md max-w-md mx-auto mt-6">
            <h2 className="text-2xl font-bold mb-4">Register a product</h2>
            <form>
                <div className="mb-4">
                    <label className="block text-sm font-medium" htmlFor="name">Product Name</label>
                    <input className="w-full p-2 rounded bg-[#FFCDBC] text-[#130303]" type="text" id="name" required />
                </div>
                <div className="mb-4">
                    <label className="block text-sm font-medium" htmlFor="price">Price</label>
                    <input className="w-full p-2 rounded bg-[#FFCDBC] text-[#130303]" type="number" id="price" required />
                </div>
                <button className="bg-[#F5853F] text-[#130303] px-4 py-2 rounded font-bold hover:bg-[#7C3626]">
                    Register
                </button>
            </form>
        </div>
    )
}