import React from 'react';
import { FaStar, FaStarHalfStroke, FaRegStar } from 'react-icons/fa6';

function StarRate({ rate }) {
  return (
    <div className="flex items-center gap-1 text-orange-400">
      {rate >= 1 ? (
        <FaStar />
      ) : rate >= 0.5 ? (
        <FaStarHalfStroke />
      ) : (
        <FaRegStar />
      )}
      {rate >= 2 ? (
        <FaStar />
      ) : rate >= 1.5 ? (
        <FaStarHalfStroke />
      ) : (
        <FaRegStar />
      )}
      {rate >= 3 ? (
        <FaStar />
      ) : rate >= 2.5 ? (
        <FaStarHalfStroke />
      ) : (
        <FaRegStar />
      )}
      {rate >= 4 ? (
        <FaStar />
      ) : rate >= 3.5 ? (
        <FaStarHalfStroke />
      ) : (
        <FaRegStar />
      )}
      {rate >= 5 ? (
        <FaStar />
      ) : rate >= 4.5 ? (
        <FaStarHalfStroke />
      ) : (
        <FaRegStar />
      )}
    </div>
  );
}

export default StarRate;
