on('ready',()=>{
    const simpleObj = (o)=>JSON.parse(JSON.stringify(o));
    const getCleanImgsrc = (imgsrc) => {
        let parts = imgsrc.match(/(.*\/images\/.*)(thumb|med|original|max)([^?]*)(\?[^?]+)?$/);
        if(parts) {
            return parts[1]+'thumb'+parts[3]+(parts[4]?parts[4]:`?${Math.round(Math.random()*9999999)}`);
        }
        return;
    };
    const duplicateCharacter = (o) => {
        let c = simpleObj(o.character);
        let oldCid = o.character.id;
        delete c.id;
        c.name=`${c.name} (COPY)`;
        c.avatar=getCleanImgsrc(c.avatar)||'';

        let newC = createObj('character',c);
        o.token.set('represents',newC.id);
        o.token.set('showname', true);
        setDefaultTokenForCharacter(newC,o.token);
        o.token.set('represents',oldCid);

        _.each(findObjs({type:'attribute',characterid:oldCid}),(a)=>{
            let sa = simpleObj(a);
            delete sa.id;
            delete sa._type;
            delete sa._characterid;
            sa.characterid = newC.id;
            createObj('attribute',sa);
        });
        _.each(findObjs({type:'ability',characterid:oldCid}),(a)=>{
            let sa = simpleObj(a);
            delete sa.id;
            delete sa._type;
            delete sa._characterid;
            sa.characterid = newC.id;
            createObj('ability',sa);
        });
    };

    on('chat:message',(msg)=>{
        if('api'===msg.type && playerIsGM(msg.playerid) && /^!dup-char-by-token\b/.test(msg.content)){
            if(msg.selected){
                var colors=["red","blue","green"];
                const n = colors.length;
                for (let i = 0; i < n; i++) { 
                    log(colors[i]);
                
                _.chain(msg.selected)
                    .map((o)=>getObj('graphic',o._id))
                    .reject(_.isUndefined)
                    .map(o=>({token: o, character: getObj('character',o.get('represents'))}))
                    .reject(o=>_.isUndefined(o.character))
                    .tap(o=>{
                        if(!o.length){
                            sendChat('',`/w gm <div style="color: #993333;font-weight:bold;">Please select one or more tokens which represent characters.</div>`);
                        } else {
                            sendChat('',`/w gm <div style="color: #993333;font-weight:bold;">Duplicating: ${o.map((obj)=>obj.character.get('name')).join(', ')} ${i+1}/${n}</div>`);
                        }
                    })
                    .each(duplicateCharacter);
                }
            } else {
                sendChat('',`/w gm <div style="color: #993333;font-weight:bold;">Please select one or more tokens.</div>`);
            }
        }
    });
});