import { PropagateLoader } from 'react-spinners';

function BigLoader() {
  return (
    <div className="w-full py-4 px-2 flex-colo h-screen">
      <PropagateLoader color="#07b8db" />
    </div>
  );
}

export default BigLoader;
