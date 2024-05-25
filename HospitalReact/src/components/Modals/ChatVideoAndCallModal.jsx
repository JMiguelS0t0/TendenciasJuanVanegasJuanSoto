
import Modal from './Modal';
import { FiPhoneCall } from 'react-icons/fi';
import { FaTimes } from 'react-icons/fa';
function ChatVideoAndCall({ closeModal, isOpen, video }) {
  return (
    <Modal closeModal={closeModal} isOpen={isOpen} width={'max-w-xl'}>
      <div className="space-y-4 flex-colo pb-12 ">
        {!video ? (
          <>
            <img
              className="w-28 h-28 rounded-full border object-cover"
              alt="user"
              src="/images/user1.png"
            />
            <h2 className="font-semibold">Minah Mmassy</h2>
            <p className="text-subMain text-xs">Calling....</p>
            <div className="flex-rows gap-4">
              <button
                onClick={() => {
                  closeModal();
                }}
                className="bg-subMain text-white w-10 h-10 flex-colo rounded-full"
              >
                <FiPhoneCall />
              </button>
              <button
                onClick={() => {
                  closeModal();
                }}
                className="bg-red-500 text-white w-10 h-10 flex-colo rounded-full"
              >
                <FaTimes />
              </button>
            </div>
          </>
        ) : (
          <>
            <img
              className="w-full h-96 rounded border object-cover"
              alt="user"
              src="/images/user1.png"
            />
            <h2 className="font-semibold">Minah Mmassy</h2>
            <p className="text-subMain text-xs">Calling....</p>
            <div className="flex-rows gap-4">
              <button
                onClick={() => {
                  closeModal();
                }}
                className="bg-subMain text-white w-10 h-10 flex-colo rounded-full"
              >
                <FiPhoneCall />
              </button>
              <button
                onClick={() => {
                  closeModal();
                }}
                className="bg-red-500 text-white w-10 h-10 flex-colo rounded-full"
              >
                <FaTimes />
              </button>
            </div>
          </>
        )}
      </div>
    </Modal>
  );
}

export default ChatVideoAndCall;
