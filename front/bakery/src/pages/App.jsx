import { Navbar } from "../components/Navbar";
import { Form } from "../components/Form";

export default function App() {
  return (
    <>
      <Navbar />
      <div className="p-6 bg-[#7C3626] text-[#FFCDBC] min-h-screen">
        <Form />
      </div>
    </>
  );
}