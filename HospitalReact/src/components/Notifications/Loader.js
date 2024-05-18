import { ScaleLoader } from 'react-spinners';

function Loader() {
  return (
    <div className="w-full py-4 px-2 flex-colo">
      <ScaleLoader color="#07b8db" />
    </div>
  );
}

export default Loader;
