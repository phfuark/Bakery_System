import { useState } from "react";

export function Navbar() {
  const [dropdown, setDropdown] = useState(false)

  function toggleDropdown() {
    setDropdown(!dropdown)
  }
  return (
    <nav className="bg-[#130303] text-[#FFCDBC] p-4 flex justify-between items-center shadow-lg">
      <div className="text-2xl font-bold">Padoc</div>
      <ul className="flex space-x-6">
        <li className="hover:text-[#F5853F] cursor-pointer">Home</li>
        <div className="flex relative ">
          <li
            className="hover:text-[#F5853F] cursor-pointer"
            onClick={toggleDropdown}
          >Registers</li>
          {dropdown && (
            <ul className="absolute top-7 bg-[#F5853F] cursor-pointer flex flex-col gap-2 px-2">
              <li>Product</li>
              <li>Card</li>
              <li>Supplier</li>
              <li>Employee</li>
            </ul>
          )}
        </div>
        <li className="hover:text-[#F5853F] cursor-pointer">Sale</li>
      </ul>
    </nav>
  );
}

