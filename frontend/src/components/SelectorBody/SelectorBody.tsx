import React, { useState } from "react";
import Man from "./Body/Man";
import "./SelectorBody.scss";

const SelectorBody: React.FC = () => {
  const [selectBodyPart, setSelectBodyPart] = useState<string>("");
  return (
    <div className="modelHuman">
      {/* {selectBodyPart} */}
      <Man SelectBodyPart={selectBodyPart} setSelectBodyPart={setSelectBodyPart} />
    </div>
  );
};

export default SelectorBody;
