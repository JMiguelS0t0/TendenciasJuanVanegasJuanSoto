import React from 'react';
import { Button, Input, Select, Textarea } from '../Form';
import { BiChevronDown } from 'react-icons/bi';
import { toast } from 'react-hot-toast';
import { sortsDatas } from '../Datas';

const sendToData = sortsDatas?.method.map((data) => {
  return {
    id: data.id,
    name: data.name,
    value: data.name,
  };
});

function WhatsappComp({ data }) {
  const [sendTo, setSendTo] = React.useState(sendToData[0]);

  // useEffect
  React.useEffect(() => {
    if (data?.id) {
      setSendTo(data.sendTo);
    }
  }, [data]);
  return (
    <div className="flex flex-col gap-4 w-full mt-4">
      {/* title */}
      <Input
        label="Campaign Title"
        color={true}
        placeholder={data?.id && data?.title}
      />
      {/* send to */}
      <div className="flex flex-col w-full gap-3">
        <p className="text-sm">Send To</p>
        <Select
          selectedPerson={sendTo}
          setSelectedPerson={setSendTo}
          datas={sendToData}
        >
          <div className="h-14 w-full text-xs text-main rounded-md bg-white border border-border px-4 flex items-center justify-between">
            <p>{sendTo?.name}</p>
            <BiChevronDown className="text-xl" />
          </div>
        </Select>
      </div>

      {/* message */}
      <Textarea
        label="Message"
        placeholder={
          data?.id ? data?.action?.message : 'Dear Delight patient ....'
        }
        color={true}
        rows={5}
      />
      {/* button */}
      {!data?.id && (
        <Button
          label={'Send Campaign'}
          onClick={() => {
            toast.error('This feature is not available yet');
          }}
        />
      )}
    </div>
  );
}

export default WhatsappComp;
