import React from "react";

function ConfirmationModal({ isOpen, onCancel, onConfirm }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white p-8 rounded-md shadow-md">
        <p className="mb-4">¿Estás seguro de que deseas eliminar este elemento?</p>
        <div className="flex justify-end">
          <button onClick={onCancel} className="mr-4 px-4 py-2 bg-gray-300 hover:bg-gray-400 rounded-md">Cancelar</button>
          <button onClick={onConfirm} className="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md">Confirmar</button>
        </div>
      </div>
    </div>
  );
}

export default ConfirmationModal;
