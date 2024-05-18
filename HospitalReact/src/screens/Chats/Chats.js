import React from 'react';
import Layout from '../../Layout';
import SideBarChat from './SideBarChat';
import Coversation from './Coversation';

function Chats() {
  return (
    <Layout>
      <div
        // data-aos="fade-left"
        // data-aos-duration="1000"
        // data-aos-delay="100"
        // data-aos-offset="200"
        className="xl:flex bg-white rounded-xl border-[1px] border-border p-5 gap-4"
      >
        {/* sidebar */}
        <div className="2xl:w-[20%] xl:w-[30%] ">
          <SideBarChat />
        </div>
        {/* chats */}
        <div className="2xl:w-[80%] xl:w-[70%] bg-slate-50 sm:p-6 p-2 rounded-lg xl:mt-0 mt-6">
          <Coversation />
        </div>
      </div>
    </Layout>
  );
}

export default Chats;
