import React from 'react';
import { BiChevronDown } from 'react-icons/bi';
import Layout from '../Layout';
import { ReviewTable } from '../components/Tables';
import { reviewData, sortsDatas } from '../components/Datas';
import { Button, Select } from '../components/Form';
import { MdOutlineCloudDownload } from 'react-icons/md';
import toast from 'react-hot-toast';

function Reviews() {
  const [star, setStar] = React.useState(sortsDatas.star[0]);
  const [user, setUser] = React.useState(sortsDatas.users[0]);

  return (
    <Layout>
      <h1 className="text-xl font-semibold">Reviews</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        <div className="grid md:grid-cols-6 grid-cols-1 gap-2">
          <div className="md:col-span-5 grid lg:grid-cols-4 xs:grid-cols-2 items-center gap-2">
            <Select
              selectedPerson={user}
              setSelectedPerson={setUser}
              datas={sortsDatas.users}
            >
              <div className="w-full flex-btn text-main text-sm p-4 border bg-dry border-border font-light rounded-lg focus:border focus:border-subMain">
                {user?.name} <BiChevronDown className="text-xl" />
              </div>
            </Select>
            <Select
              selectedPerson={star}
              setSelectedPerson={setStar}
              datas={sortsDatas.star}
            >
              <div className="w-full flex-btn text-main text-sm p-4 border bg-dry border-border font-light rounded-lg focus:border focus:border-subMain">
                {star?.name} <BiChevronDown className="text-xl" />
              </div>
            </Select>
          </div>

          {/* export */}
          <Button
            label="Export"
            Icon={MdOutlineCloudDownload}
            onClick={() => {
              toast.error('Exporting is not available yet');
            }}
          />
        </div>
        {/* datas */}

        <div className="mt-8 w-full overflow-x-scroll">
          <ReviewTable doctor={false} data={reviewData} />
        </div>
      </div>
    </Layout>
  );
}

export default Reviews;
