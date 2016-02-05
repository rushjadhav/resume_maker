<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1449224944783" ID="ID_988385840" MODIFIED="1454583412190" TEXT="Online resume maker">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Following are the applications
    </p>
    <p>
      
    </p>
    <p>
      1. Profile Management (pm):
    </p>
    <p>
      &#160;&#160;&#160;&#160;- Manages users personal information, skills as well as languages
    </p>
    <p>
      
    </p>
    <p>
      2. Experience Management (em):
    </p>
    <p>
      &#160;&#160;&#160;- Manages users industrial experience.
    </p>
    <p>
      
    </p>
    <p>
      3. Education Management (edm):
    </p>
    <p>
      &#160;&#160;&#160;- Manages users education details.
    </p>
    <p>
      
    </p>
    <p>
      4. Resume_management (rm):
    </p>
    <p>
      &#160;&#160;&#160;- Manages resume templates and resumes of users.
    </p>
    <p>
      
    </p>
    <p>
      5. Commercial (co):
    </p>
    <p>
      &#160;&#160;&#160;- Manages pricing and accounting related things.
    </p>
  </body>
</html>
</richcontent>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452758905700" FOLDED="true" HGAP="29" ID="ID_1488833699" MODIFIED="1454583649740" POSITION="right" TEXT="Address(pm)">
<node CREATED="1452845001652" ID="ID_1696437387" MODIFIED="1453445149725" TEXT="id: pk, ai, unique"/>
<node CREATED="1452758936909" ID="ID_931402131" MODIFIED="1452758946176" TEXT="address1: varchar(40), not null"/>
<node CREATED="1452758936909" ID="ID_1398348960" MODIFIED="1452846080239" TEXT="address2: varchar(40), null"/>
<node CREATED="1452758936909" ID="ID_1239031463" MODIFIED="1452846083284" TEXT="address3: varchar(40),  null"/>
<node CREATED="1452845048339" ID="ID_418857767" MODIFIED="1453451242358" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452758844741" FOLDED="true" ID="ID_992628570" MODIFIED="1454583649740" POSITION="right" TEXT="PhoneNumber(pm)">
<node CREATED="1452845001652" ID="ID_1957478273" MODIFIED="1453445235028" TEXT="id: pk, ai, unique"/>
<node CREATED="1452758785261" ID="ID_1622749993" MODIFIED="1452847117449" TEXT="phone_number: varchar(20), not null, unique"/>
<node CREATED="1452845048339" ID="ID_720458540" MODIFIED="1453451242354" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1452844867500" FOLDED="true" ID="ID_383058277" MODIFIED="1454583649741" POSITION="left" TEXT="Company(em)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Represents an organization
    </p>
    <p>
      e.g: Infosys, L&amp;T
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_923563396" MODIFIED="1452848299072" TEXT="id: pk,ai, unique"/>
<node CREATED="1452844914444" ID="ID_772799294" MODIFIED="1452844957212" TEXT="name: varchar(120), not null, unique"/>
<node CREATED="1452845309089" ID="ID_563801441" MODIFIED="1453450353134" TEXT="date of establishment: varchar(40), null"/>
<node CREATED="1452846244395" ID="ID_1484541146" MODIFIED="1453450446950" TEXT="email: fk(email: id), null"/>
<node CREATED="1452846276570" ID="ID_10864839" MODIFIED="1453450451141" TEXT="phone_number: fk(PhoneNumber: id), null">
<arrowlink DESTINATION="ID_1957478273" ENDARROW="Default" ENDINCLINATION="283;0;" ID="Arrow_ID_1746292718" STARTARROW="None" STARTINCLINATION="283;0;"/>
</node>
<node CREATED="1452846311146" ID="ID_320306666" MODIFIED="1453450454453" TEXT="addresse: fk(Address: id), null"/>
<node CREATED="1452845048339" ID="ID_139284637" MODIFIED="1453451242350" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1452848226021" FOLDED="true" ID="ID_717737212" MODIFIED="1454583649741" POSITION="left" TEXT="Experience(em)">
<node CREATED="1449225361162" ID="ID_1402588316" MODIFIED="1452846344829" TEXT="id: int, ai, pk"/>
<node CREATED="1452844606038" ID="ID_1631947363" MODIFIED="1452848258335" TEXT="user: fk(user:id), not null ">
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="699;0;" ID="Arrow_ID_401472878" STARTARROW="None" STARTINCLINATION="699;0;"/>
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="699;0;" ID="Arrow_ID_839795944" STARTARROW="None" STARTINCLINATION="699;0;"/>
</node>
<node CREATED="1452848263165" ID="ID_963428625" MODIFIED="1452848307032" TEXT="company: fk(Company: id), not null">
<arrowlink DESTINATION="ID_923563396" ENDARROW="Default" ENDINCLINATION="388;0;" ID="Arrow_ID_626478900" STARTARROW="None" STARTINCLINATION="388;0;"/>
</node>
<node CREATED="1452848330877" ID="ID_200745084" MODIFIED="1452848341329" TEXT="worked_from: date_time, not null"/>
<node CREATED="1452848344076" ID="ID_899505652" MODIFIED="1453450916138" TEXT="worked_upto: date_time, null"/>
<node CREATED="1452848379492" ID="ID_141991686" MODIFIED="1453451242347" TEXT="designation: varchar(40), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g: Senior Software engineer
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1452845048339" ID="ID_792873876" MODIFIED="1453451242346" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1452846741559" FOLDED="true" ID="ID_1949073153" MODIFIED="1454583649742" POSITION="left" TEXT="Institude(edum)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Represents an educational institude
    </p>
    <p>
      
    </p>
    <p>
      e.g. IIT Bombay, D.Y patil College of engineering Pune
    </p>
  </body>
</html></richcontent>
<node CREATED="1449225361162" ID="ID_763067130" MODIFIED="1453451354002" TEXT="id: int, ai, pk"/>
<node CREATED="1452844914444" ID="ID_106889195" MODIFIED="1452844957212" TEXT="name: varchar(120), not null, unique"/>
<node CREATED="1452845309089" ID="ID_65845001" MODIFIED="1452845359611" TEXT="date of establishment: varchar(40), not null"/>
<node CREATED="1452846244395" ID="ID_1168059339" MODIFIED="1452846272654" TEXT="emails: fk(email: id), null"/>
<node CREATED="1452846276570" ID="ID_1367448470" MODIFIED="1452846302230" TEXT="phone_numbers: fk(PhoneNumber: id), null">
<arrowlink DESTINATION="ID_1957478273" ENDARROW="Default" ENDINCLINATION="283;0;" ID="Arrow_ID_1115348158" STARTARROW="None" STARTINCLINATION="283;0;"/>
</node>
<node CREATED="1452846311146" ID="ID_701593005" MODIFIED="1452846372902" TEXT="addresses: fk(Address: id), null"/>
<node CREATED="1452845048339" ID="ID_1110000129" MODIFIED="1453451242342" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844493096" FOLDED="true" ID="ID_746338025" MODIFIED="1454583649742" POSITION="right" TEXT="Hobby(pm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g: HTML, CSS, designing,
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844503103" ID="ID_834621902" MODIFIED="1453373364509" TEXT="id: pk, ai, unique"/>
<node CREATED="1452844521767" ID="ID_1462954540" MODIFIED="1452844533985" TEXT="name: varchar(120), not null, unique"/>
<node CREATED="1452845048339" ID="ID_791891583" MODIFIED="1453451242338" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844493096" FOLDED="true" ID="ID_575501081" MODIFIED="1454583649743" POSITION="right" TEXT="Skill(pm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g: HTML, CSS, designing,
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844503103" ID="ID_499033636" MODIFIED="1453373332809" TEXT="id: pk, ai, unique"/>
<node CREATED="1452844521767" ID="ID_497584462" MODIFIED="1452844533985" TEXT="name: varchar(120), not null, unique"/>
<node CREATED="1452845048339" ID="ID_1440701935" MODIFIED="1453451242337" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844493096" FOLDED="true" ID="ID_1434349496" MODIFIED="1454583649743" POSITION="right" TEXT="Language(pm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g.: English, jerman
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844503103" ID="ID_1977859390" MODIFIED="1452847511126" TEXT="id: pk, ai, unique"/>
<node CREATED="1452844521767" ID="ID_179103853" MODIFIED="1452844533985" TEXT="name: varchar(120), not null, unique"/>
<node CREATED="1452845048339" ID="ID_444219282" MODIFIED="1453451242333" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1449224979213" FOLDED="true" HGAP="26" ID="ID_898605628" MODIFIED="1454583649744" POSITION="right" TEXT="User(pm)" VSHIFT="2">
<node CREATED="1449225361162" ID="ID_1203191758" MODIFIED="1452846344829" TEXT="id: int, ai, pk"/>
<node CREATED="1449224989117" ID="ID_185946092" MODIFIED="1449225019277" TEXT="username: varchar(60), unique, not null"/>
<node CREATED="1449224994117" ID="ID_1164614064" MODIFIED="1453114330258" TEXT="first_name: varchar(30), not null"/>
<node CREATED="1449224994117" ID="ID_1557567512" MODIFIED="1453114333220" TEXT="middle_name: varchar(30), null"/>
<node CREATED="1449224998845" ID="ID_1428449152" MODIFIED="1453114335480" TEXT="last_name: varchar(30), null"/>
<node CREATED="1449225168635" ID="ID_1153813114" MODIFIED="1449225180230" TEXT="profile_pic: imagefield, null"/>
<node CREATED="1452758471472" ID="ID_1414421041" MODIFIED="1453113922117" TEXT="date_of_birth: varchar(40), not null"/>
<node CREATED="1452758619886" ID="ID_839904603" MODIFIED="1452758631590" TEXT="nationality: varchar(40), not null"/>
<node CREATED="1452845048339" ID="ID_1063838857" MODIFIED="1453451242331" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1452848226021" FOLDED="true" ID="ID_758554560" MODIFIED="1454583649744" POSITION="left" TEXT="Education(edum)">
<node CREATED="1449225361162" ID="ID_343835445" MODIFIED="1452846344829" TEXT="id: int, ai, pk"/>
<node CREATED="1452844606038" ID="ID_1896128789" MODIFIED="1452848258335" TEXT="user: fk(user:id), not null ">
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="699;0;" ID="Arrow_ID_1883351357" STARTARROW="None" STARTINCLINATION="699;0;"/>
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="699;0;" ID="Arrow_ID_690951568" STARTARROW="None" STARTINCLINATION="699;0;"/>
</node>
<node CREATED="1453451338454" ID="ID_1771700186" MODIFIED="1453451359862" TEXT="institude: fk(institude: id), not null">
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="321;0;" ID="Arrow_ID_463188455" STARTARROW="None" STARTINCLINATION="321;0;"/>
</node>
<node CREATED="1452848330877" ID="ID_1437653513" MODIFIED="1452848497812" TEXT="from_date: date_time, not null"/>
<node CREATED="1452848344076" ID="ID_707372737" MODIFIED="1452848504046" TEXT="to_date: date_time, not null"/>
<node CREATED="1452848379492" ID="ID_656880022" MODIFIED="1453451359646" TEXT="course_name: varchar(40), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g: BE Computer Science
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1452845048339" ID="ID_1631924525" MODIFIED="1453451358654" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1452861044293" FOLDED="true" ID="ID_1240395015" MODIFIED="1454583649745" POSITION="left" TEXT="ResumeTemplate(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Sample template of resume or cv.
    </p>
  </body>
</html></richcontent>
<node CREATED="1449225361162" ID="ID_1561223769" MODIFIED="1452861212504" TEXT="id: int, ai, pk"/>
<node CREATED="1452845422208" ID="ID_428400540" MODIFIED="1452845468440" TEXT="name: varchar(60), not null, unique"/>
<node CREATED="1453104536172" ID="ID_887719123" MODIFIED="1453451242324" TEXT="code: varchar(30), not null, unique">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique code for template.
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1453359047444" ID="ID_45365320" MODIFIED="1453359076127" TEXT="display_pic: imagefield, not null"/>
<node CREATED="1453377003438" ID="ID_524550419" MODIFIED="1453377016321" TEXT="description: textfield, null"/>
<node CREATED="1452845048339" ID="ID_973778642" MODIFIED="1453451242322" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1452861163580" FOLDED="true" ID="ID_1916135802" MODIFIED="1454583649746" POSITION="left" TEXT="Resume(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Actual resume of an user.
    </p>
    <p>
      unique(name, user)
    </p>
  </body>
</html></richcontent>
<node CREATED="1449225361162" ID="ID_734593427" MODIFIED="1453441274159" TEXT="id: int, ai, pk"/>
<node CREATED="1452845422208" ID="ID_1182922014" MODIFIED="1452861234301" TEXT="name: varchar(60), not null"/>
<node CREATED="1452844606038" ID="ID_1201497476" MODIFIED="1453451242320" TEXT="user: fk(user:id), not null ">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unuique(name, user)
    </p>
  </body>
</html></richcontent>
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="699;0;" ID="Arrow_ID_1079309151" STARTARROW="None" STARTINCLINATION="699;0;"/>
<arrowlink DESTINATION="ID_763067130" ENDARROW="Default" ENDINCLINATION="699;0;" ID="Arrow_ID_985193144" STARTARROW="None" STARTINCLINATION="699;0;"/>
</node>
<node CREATED="1452861194132" ID="ID_487705365" MODIFIED="1453446875294" TEXT="resume_template: fk(resume_template: id) null">
<arrowlink DESTINATION="ID_1561223769" ENDARROW="Default" ENDINCLINATION="217;0;" ID="Arrow_ID_911550050" STARTARROW="None" STARTINCLINATION="217;0;"/>
</node>
<node CREATED="1452861270140" ID="ID_1941950994" MODIFIED="1453451242318" STYLE="fork" TEXT="is_published: boolean, default F, not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      If set to true resume will be accesssible to everybody.
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1453108848741" ID="ID_942427271" MODIFIED="1453451242316" TEXT="access_url: varchar(120), not null, unique">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Users can share this url with others.
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1453358877127" ID="ID_210235214" MODIFIED="1453358906023" TEXT="number_of_views: integer, default 0, not null"/>
<node CREATED="1453448317339" ID="ID_995133811" MODIFIED="1453459170243" TEXT="career_objective: textfield, null"/>
<node CREATED="1452845048339" ID="ID_1691391303" MODIFIED="1453459170249" TEXT="status: varchar(1), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Active: A
    </p>
    <p>
      InActive: I
    </p>
    <p>
      Deleted: D
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844573807" FOLDED="true" ID="ID_1540646998" MODIFIED="1454583649746" POSITION="left" TEXT="ResumeSkillMap(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(skill, resume)
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_888627109" MODIFIED="1453441271592" TEXT="id: pk,ai, unique"/>
<node CREATED="1452844626958" ID="ID_1950153181" MODIFIED="1452844655914" TEXT="skill: fk(skill: id), not null">
<arrowlink DESTINATION="ID_499033636" ENDARROW="Default" ENDINCLINATION="142;0;" ID="Arrow_ID_1762554672" STARTARROW="None" STARTINCLINATION="142;0;"/>
</node>
<node CREATED="1453441236845" ID="ID_923060983" MODIFIED="1453441280951" TEXT="resume: fk(resume:id), not null">
<arrowlink DESTINATION="ID_734593427" ENDARROW="Default" ENDINCLINATION="298;0;" ID="Arrow_ID_1676157219" STARTARROW="None" STARTINCLINATION="298;0;"/>
</node>
<node CREATED="1452844671686" ID="ID_895856745" MODIFIED="1452844697690" TEXT="eficcency_level; integer, not null"/>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844573807" FOLDED="true" ID="ID_617220616" MODIFIED="1454583649746" POSITION="left" TEXT="ResumeLanguageMap(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(language, user)
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_700224442" MODIFIED="1452844595950" TEXT="id: pk,ai, unique"/>
<node CREATED="1452844626958" ID="ID_1121204213" MODIFIED="1452847511126" TEXT="language: fk(language: id), not null">
<arrowlink DESTINATION="ID_1977859390" ENDARROW="Default" ENDINCLINATION="273;0;" ID="Arrow_ID_390416336" STARTARROW="None" STARTINCLINATION="273;0;"/>
</node>
<node CREATED="1453441236845" ID="ID_1014991832" MODIFIED="1453441287451" TEXT="resume: fk(resume:id), not null">
<arrowlink DESTINATION="ID_734593427" ENDARROW="Default" ENDINCLINATION="298;0;" ID="Arrow_ID_1378104190" STARTARROW="None" STARTINCLINATION="298;0;"/>
</node>
<node CREATED="1452844671686" ID="ID_1291352777" MODIFIED="1452844697690" TEXT="eficcency_level; integer, not null"/>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844573807" FOLDED="true" ID="ID_777426095" MODIFIED="1454583649747" POSITION="left" TEXT="ResumeHobbyMap(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(skill, user)
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_1754600638" MODIFIED="1452844595950" TEXT="id: pk,ai, unique"/>
<node CREATED="1453441236845" ID="ID_1589734548" MODIFIED="1453441296041" TEXT="resume: fk(resume:id), not null">
<arrowlink DESTINATION="ID_734593427" ENDARROW="Default" ENDINCLINATION="298;0;" ID="Arrow_ID_47202916" STARTARROW="None" STARTINCLINATION="298;0;"/>
</node>
<node CREATED="1452844626958" ID="ID_71656347" MODIFIED="1453373364510" TEXT="hobby: fk(hobby: id), not null">
<arrowlink DESTINATION="ID_834621902" ENDARROW="Default" ENDINCLINATION="659;0;" ID="Arrow_ID_1289654565" STARTARROW="None" STARTINCLINATION="659;0;"/>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844573807" FOLDED="true" ID="ID_591054258" MODIFIED="1454583649747" POSITION="left" TEXT="ResumeEmailMap(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(email, resume)
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_333843739" MODIFIED="1452844595950" TEXT="id: pk,ai, unique"/>
<node CREATED="1453441236845" ID="ID_496530135" MODIFIED="1453441296041" TEXT="resume: fk(resume:id), not null">
<arrowlink DESTINATION="ID_734593427" ENDARROW="Default" ENDINCLINATION="298;0;" ID="Arrow_ID_894464592" STARTARROW="None" STARTINCLINATION="298;0;"/>
</node>
<node CREATED="1453445012650" ID="ID_196929241" MODIFIED="1453445027533" TEXT="email: fk(email:id), not null"/>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844573807" FOLDED="true" ID="ID_1074844630" MODIFIED="1454583649748" POSITION="left" TEXT="ResumeAddressMap(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(resume, address)
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_1154425423" MODIFIED="1452844595950" TEXT="id: pk,ai, unique"/>
<node CREATED="1453441236845" ID="ID_897839355" MODIFIED="1453441296041" TEXT="resume: fk(resume:id), not null">
<arrowlink DESTINATION="ID_734593427" ENDARROW="Default" ENDINCLINATION="298;0;" ID="Arrow_ID_1928388284" STARTARROW="None" STARTINCLINATION="298;0;"/>
</node>
<node CREATED="1453445064329" ID="ID_1406275747" MODIFIED="1453445149725" TEXT="address: fk(address: id), not null">
<arrowlink DESTINATION="ID_1696437387" ENDARROW="Default" ENDINCLINATION="1230;0;" ID="Arrow_ID_1791374308" STARTARROW="None" STARTINCLINATION="1230;0;"/>
</node>
</node>
<node BACKGROUND_COLOR="#ffffff" CREATED="1452844573807" FOLDED="true" ID="ID_1836113558" MODIFIED="1454583649748" POSITION="left" TEXT="ResumePhoneNumberMap(rm)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(resume, phone_number)
    </p>
  </body>
</html></richcontent>
<node CREATED="1452844586238" ID="ID_289864728" MODIFIED="1452844595950" TEXT="id: pk,ai, unique"/>
<node CREATED="1453441236845" ID="ID_352851265" MODIFIED="1453441296041" TEXT="resume: fk(resume:id), not null">
<arrowlink DESTINATION="ID_734593427" ENDARROW="Default" ENDINCLINATION="298;0;" ID="Arrow_ID_244636351" STARTARROW="None" STARTINCLINATION="298;0;"/>
</node>
<node CREATED="1453445211824" ID="ID_742671633" MODIFIED="1453445235028" TEXT="phone_number: fk(phone_number: id), not null">
<arrowlink DESTINATION="ID_1957478273" ENDARROW="Default" ENDINCLINATION="1253;0;" ID="Arrow_ID_1672872407" STARTARROW="None" STARTINCLINATION="1253;0;"/>
</node>
</node>
</node>
</map>
